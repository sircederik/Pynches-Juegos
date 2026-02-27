class MonopolyEngine:
    def __init__(self, jugadores, tablero, mazo_suerte, mazo_arca, dados, cobro_salida, verbosity=1):
        self.jugadores = jugadores
        self.tablero = tablero
        self.mazo_suerte = mazo_suerte
        self.mazo_arca = mazo_arca
        self.dados = dados
        self.monto_salida = cobro_salida
        self.verbosity = verbosity
        # Mapeo de acciones del JSON a métodos internos
        self.despachador_cartas = {
            "mover_a": self._accion_mover_a,
            "mover_relativo": self._accion_mover_relativo,
            "mover_a_tipo": self._accion_mover_a_tipo,
            "cobrar": self._accion_cobrar,
            "pagar": self._accion_pagar,
            "ir_a_carcel": self._accion_ir_a_carcel,
            "cobrar_de_todos": self._accion_cobrar_de_todos,
            "pagar_a_todos": self._accion_pagar_a_todos,
            "impuesto_propiedades": self._accion_impuesto_propiedades
        }

    def _log(self, mensaje, nivel_requerido):
        """Método auxiliar para centralizar los prints según verbosidad."""
        if self.verbosity >= nivel_requerido:
            print(mensaje)

    def ejecutar_partida(self, max_turnos=1000):
        for t in range(max_turnos):
            jugadores_activos = [j for j in self.jugadores if not j.esta_quebrado]

        # Si solo queda uno (o ninguno), la partida termina
            if len(jugadores_activos) <= 1:
                self._log(f"\n[!] Simulación terminada en turno {t}: Solo queda un superviviente.", 1)
                break

            for jugador in jugadores_activos:
                self.jugar_turno(jugador)

    def jugar_turno(self, jugador):
        """Lógica de un turno individual."""
        # 1. Tirar dados
        suma, es_doble = self.dados.tirar()

        self._log(f"[DEBUG] {jugador.nombre} lanza {suma}", 3)

       # 2. El jugador procesa su estado (cárcel, posición, contador de visitas)
        jugador.lanzar_dados(suma, es_doble)

        # 3. Si no terminó en la cárcel por los dados, procesar la casilla de aterrizaje
        if not jugador.en_carcel:
            if self.verbosity >= 2:
                casilla = self.tablero[jugador.posicion]["nombre"]
                self._log(f"[INFO] {jugador.nombre} aterrizó en {casilla}", 2)
            self._procesar_casilla(jugador)

    def _procesar_propiedad(self, jugador, casilla):
        dueno = casilla.get("dueno")

            # 2. Si no hay dueño (es None), el jugador puede comprar
        if dueno is None:
            precio = casilla.get("precio", 0)
            if jugador.dinero >= precio:
                jugador.pagar(precio)
                # IMPORTANTE: Guardamos al objeto jugador como dueño en el diccionario
                casilla["dueno"] = jugador

                # También lo registramos en el inventario del jugador si tienes esa lista
                if hasattr(jugador, 'propiedades'):
                    jugador.propiedades.append(casilla["nombre"])

                self._log(f"[ECONOMÍA] {jugador.nombre} compró {casilla['nombre']} por ${precio}", 2)

        # 3. Si hay dueño y NO es el jugador actual, se paga renta
        elif dueno != jugador and not dueno.esta_quebrado:
            # Obtenemos la renta (usamos 0 por defecto si no está definida)
            renta = casilla.get("renta", 0)

            self._log(f"[PAGO] {jugador.nombre} paga ${renta} a {dueno.nombre} por {casilla['nombre']}", 2)

            # Realizamos la transferencia de dinero
            jugador.pagar(renta, destinatario=dueno)



    def _procesar_casilla(self, jugador):
        """Identifica el tipo de casilla y aplica la regla correspondiente."""
        casilla = self.tablero[jugador.posicion]
        tipo = casilla["tipo"]

        # 2. Despachar según el tipo de casilla
        if tipo in ["calle", "ferrocarril", "servicio"]:
            # AQUÍ es donde llamas a la lógica económica
            self._procesar_propiedad(jugador, casilla)

        if tipo == "suerte":
            self._ejecutar_carta(jugador, self.mazo_suerte)
        elif tipo == "arca":
            self._ejecutar_carta(jugador, self.mazo_arca)
        elif tipo == "impuesto":
            jugador.pagar(casilla.get("precio", 100))
        elif tipo == "especial" and casilla["nombre"] == "Váyase a la Cárcel":
            jugador.ir_a_la_carcel()

    def _ejecutar_carta(self, jugador, mazo):
        """Saca una carta del mazo y busca su función en el despachador."""
        carta = mazo.sacar_carta()

        if self.verbosity >= 2:
            tipo = "SUERTE" if mazo == self.mazo_suerte else "ARCA"
            print(f"[CARTA] {jugador.nombre} sacó de {tipo}: {carta['nombre']}")

        accion = carta.get("accion")

        if accion in self.despachador_cartas:
            self.despachador_cartas[accion](jugador, carta)

    # --- MÉTODOS DE ACCIÓN (Lógica de las cartas del JSON) ---

    def _accion_mover_a(self, jugador, carta):
        destino = carta["destino"]
        # Si pasa por salida (0) y el destino no es la cárcel (10)
        if destino < jugador.posicion and destino != 10:
            jugador.pagar(-self.monto_salida) # Cobrar Salida
        jugador.mover_a(destino)

    def _accion_mover_relativo(self, jugador, carta):
        nueva_pos = (jugador.posicion + carta["valor"]) % 40
        jugador.mover_a(nueva_pos)

    def _accion_mover_a_tipo(self, jugador, carta):
        tipo_buscado = carta["tipo"]
        pos_actual = jugador.posicion
        for i in range(1, 41):
            nueva_pos = (pos_actual + i) % 40
            if self.tablero[nueva_pos]["tipo"] == tipo_buscado:
                if nueva_pos < pos_actual:
                    jugador.pagar(-self.monto_salida)
                jugador.mover_a(nueva_pos)
                break

    def _accion_cobrar(self, jugador, carta):
        jugador.pagar(-carta["valor"])

    def _accion_pagar(self, jugador, carta):
        jugador.pagar(carta["valor"])

    def _accion_ir_a_carcel(self, jugador, carta):
        jugador.ir_a_la_carcel()

    def _accion_cobrar_de_todos(self, jugador, carta):
        monto = carta["valor"]
        for j in self.jugadores:
            if j != jugador and not j.esta_quebrado:
                j.pagar(monto)
                jugador.pagar(-monto)

    def _accion_pagar_a_todos(self, jugador, carta):
        monto = carta["valor"]
        for j in self.jugadores:
            if j != jugador and not j.esta_quebrado:
                jugador.pagar(monto)
                j.pagar(-monto)

    def _accion_impuesto_propiedades(self, jugador, carta):
        # Esta lógica se activará cuando implementemos el sistema de casas
        # Por ahora, es un placeholder para que no falle el motor
        pass
