import numpy as np

class Dados:
    def __init__(self, semilla=None):
        """
        Inicializa el generador de números aleatorios de NumPy.
        Si semilla es None, el sistema usará una fuente de entropía del SO.
        """
        self.rng = np.random.default_rng(seed=semilla)

    def tirar(self):
        """
        Simula el lanzamiento de dos dados.
        Retorna:
            - suma (int): Suma de los dos dados.
            - es_doble (bool): True si son iguales.
        """
        # Generamos dos números entre 1 y 6 (endpoint es exclusivo en NumPy)
        dado1, dado2 = self.rng.integers(1, 7, size=2)
        
        suma = int(dado1 + dado2)
        es_doble = bool(dado1 == dado2)
        
        return suma, es_doble

    def generar_lote_tiradas(self, n=1000000):
        """
        Genera millones de tiradas en milisegundos para análisis masivo.
        Ideal para calcular la distribución teórica del tablero.
        """
        dados = self.rng.integers(1, 7, size=(n, 2))
        sumas = dados.sum(axis=1)
        dobles = dados[:, 0] == dados[:, 1]
        
        return sumas, dobles
