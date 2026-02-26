
class MonopolyEngine:
    def __init__(self, jugadores, tablero, mazo_suerte, mazo_arca, dados):
        self.jugadores = jugadores
        self.tablero = tablero
        self.mazo_suerte = mazo_suerte
        self.mazo_arca = mazo_arca
        self.dados = dados

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

    def ejecutar_partida(self, max_turnos=1000):
        """Bucle principal de la simulación."""
        for _ in range(max_turnos):
            for jugador in self.jugadores:
                if not jugador.esta_quebrado:
                    self.jugar_turno(jugador)

    def jugar_turno(self, jugador):
        """Lógica de un turno individual."""
        # 1. Tirar dados
        suma, es_doble = self.dados.tirar()

        # 2. El jugador procesa su estado (cárcel, posición, contador de visitas)
        jugador.lanzar_dados(suma, es_doble)

        # 3. Si no terminó en la cárcel por los dados, procesar la casilla de aterrizaje
        if not jugador.en_carcel:
            self._procesar_casilla(jugador)

    def _procesar_casilla(self, jugador):
        """Identifica el tipo de casilla y aplica la regla correspondiente."""
        casilla = self.tablero[jugador.posicion]
        tipo = casilla["tipo"]

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
        accion = carta.get("accion")

        if accion in self.despachador_cartas:
            self.despachador_cartas[accion](jugador, carta)

    # --- MÉTODOS DE ACCIÓN (Lógica de las cartas del JSON) ---

    def _accion_mover_a(self, jugador, carta):
        destino = carta["destino"]
        # Si pasa por salida (0) y el destino no es la cárcel (10)
        if destino < jugador.posicion and destino != 10:
            jugador.pagar(-200) # Cobrar Salida
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
                    jugador.pagar(-200)
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
