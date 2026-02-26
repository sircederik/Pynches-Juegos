import random
import json
import os


class Mazo:
    def __init__(self, nombre, lista_cartas, rng):
        self.nombre = nombre
        self.cartas_originales = lista_cartas
        self.mazo = list(lista_cartas)
        self.rng = rng  # Pasamos el generador de NumPy
        self.barajar()

    def barajar(self):
        # Usamos el generador de NumPy para barajar
        self.rng.shuffle(self.mazo)

    def sacar_carta(self):
        if not self.mazo:
            self.mazo = list(self.cartas_originales)
            self.barajar()
        return self.mazo.pop(0)


def cargar_paquete_de_cartas(nombre_set, rng):
    """
    Busca un archivo .json en data/card_sets/ y devuelve dos objetos Mazo.
    """
    ruta = os.path.join("data", "card_sets", f"{nombre_set}.json")

    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el set de cartas: {ruta}")

    with open(ruta, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Creamos las instancias de Mazo inyectando el RNG compartido
    mazo_suerte = Mazo("Suerte", data.get("suerte", []), rng)
    mazo_arca = Mazo("Arca Comunal", data.get("arca", []), rng)

    return mazo_suerte, mazo_arca

