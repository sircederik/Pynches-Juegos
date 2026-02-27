class Jugador:
    def __init__(self, id_jugador, nombre, dinero_inicial=1500, estrategia="estandar"):
        self.id = id_jugador
        self.nombre = nombre
        self.estrategia = estrategia

        # Estado de posición
        self.posicion = 0
        self.en_carcel = False
        self.turnos_en_carcel = 0
        self.dobles_consecutivos = 0

        # Estado financiero
        self.dinero = dinero_inicial
        self.propiedades = [] # Lista de objetos de la clase Propiedad
        self.esta_quebrado = False

        # Métricas para el estudio estadístico
        self.contador_visitas = [0] * 40 # Para generar el mapa de calor después
        self.historial_dinero = [1500]

    def mover_a(self, nueva_posicion, pasar_por_salida=True):
        """Mueve al jugador a una casilla específica (útil para cartas y cárcel)."""
        if pasar_por_salida and nueva_posicion < self.posicion:
            self.dinero += 200

        self.posicion = nueva_posicion
        self.contador_visitas[self.posicion] += 1
        self.historial_dinero.append(self.dinero)

    def lanzar_dados(self, dado1, dado2):
        """Gestiona la lógica de movimiento y la regla de los 3 dobles."""
        es_doble = (dado1 == dado2)

        if es_doble:
            self.dobles_consecutivos += 1
        else:
            self.dobles_consecutivos = 0

        # Regla de los 3 dobles (Artículos indexados la citan como factor clave)
        if self.dobles_consecutivos == 3:
            self.ir_a_la_carcel()
            return

        if self.en_carcel:
            self._gestionar_carcel(es_doble, dado1 + dado2)
        else:
            nueva_pos = (self.posicion + dado1 + dado2) % 40
            self.mover_a(nueva_pos)

    def ir_a_la_carcel(self):
        self.posicion = 10
        self.en_carcel = True
        self.turnos_en_carcel = 0
        self.dobles_consecutivos = 0
        self.contador_visitas[10] += 1

    def _gestionar_carcel(self, es_doble, suma_dados):
        """Lógica interna para intentar salir de la cárcel."""
        if es_doble:
            self.en_carcel = False
            self.mover_a((self.posicion + suma_dados) % 40)
        else:
            self.turnos_en_carcel += 1
            if self.turnos_en_carcel == 3:
                self.dinero -= 50 # Paga fianza obligatoria
                self.en_carcel = False
                self.mover_a((self.posicion + suma_dados) % 40)
            # Si no, se queda en la casilla 10 un turno más


    def pagar(self, monto, destinatario=None):
        """
        Resta monto al jugador. Si se pasa un destinatario, se le suma el monto.
        """
        if self.dinero >= monto:
            self.dinero -= monto
            if destinatario is not None:
                destinatario.dinero += monto
            return True
        else:
            # Lógica de quiebra: entrega lo que le queda al destinatario
            if destinatario is not None:
                destinatario.dinero += self.dinero

            self.dinero = 0
            self.esta_quebrado = True
            return False
