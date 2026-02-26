import os
import pandas as pd
from src.models.jugador import Jugador
from src.logic.dados import Dados
from src.logic.tablero import generar_tablero
from src.logic.cartas import cargar_paquete_de_cartas # La nueva función
from src.engine import MonopolyEngine

import os
import pandas as pd
from src.models.jugador import Jugador
from src.logic.dados import Dados
from src.logic.tablero import generar_tablero
from src.logic.cartas import cargar_paquete_de_cartas
from src.engine import MonopolyEngine

def ejecutar_experimento(num_turnos=100000, semilla=2026, set_cartas="oficial"):
    """
    Orquestador principal: Configura, simula y consolida datos.
    """
    print(f"--- Configurando Experimento (Semilla: {semilla}, Set: {set_cartas}) ---")

    # 1. Inicializar componentes de azar y reglas
    dados = Dados(semilla=semilla)
    tablero = generar_tablero()
    # Cargamos los mazos desde el JSON usando el generador de los dados
    m_suerte, m_arca = cargar_paquete_de_cartas(set_cartas, dados.rng)

    # 2. Configurar sujetos de prueba
    # Usamos 4 jugadores para una dinámica de mazo más realista
    jugadores = [Jugador(i, f"Agente_{i}") for i in range(1, 5)]

    # 3. Lanzar el motor
    engine = MonopolyEngine(jugadores, tablero, m_suerte, m_arca, dados)

    print(f"Simulando {num_turnos} turnos...")
    engine.ejecutar_partida(max_turnos=num_turnos)

    # 4. Consolidar visitas de todos los jugadores
    visitas_totales = [0] * 40
    for j in jugadores:
        for i in range(40):
            visitas_totales[i] += j.contador_visitas[i]

    return visitas_totales

def exportar_y_analizar(visitas, nombre_set):
    """
    Procesa los resultados, los guarda en CSV y muestra el análisis en consola.
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    tablero = generar_tablero()

    # Crear DataFrame
    df = pd.DataFrame({
        "ID": range(40),
        "Casilla": [c["nombre"] for c in tablero],
        "Tipo": [c["tipo"] for c in tablero],
        "Visitas": visitas
    })

    # Cálculos estadísticos
    total_visitas = df["Visitas"].sum()
    df["Probabilidad (%)"] = (df["Visitas"] / total_visitas) * 100

    # Guardar CSV
    ruta_csv = os.path.join("data", f"resultado_{nombre_set}.csv")
    df.to_csv(ruta_csv, index=False)

    # Mostrar resultados clave
    print("\n" + "="*40)
    print(f" RESULTADOS: {nombre_set.upper()}")
    print("="*40)
    print(df.sort_values("Visitas", ascending=False).head(10).to_string(index=False))
    print(f"\n[OK] Datos completos guardados en: {ruta_csv}")

if __name__ == "__main__":
    # PARÁMETROS DEL USUARIO
    TURNOS = 100_000_000  # Tus 100 millones (¡ten paciencia!)
    SEMILLA = 2026
    SET_CARTAS = "oficial" # Debe existir data/card_sets/oficial.json

    try:
        # 1. Ejecución
        datos_finales = ejecutar_experimento(TURNOS, SEMILLA, SET_CARTAS)

        # 2. Análisis y Exportación
        exportar_y_analizar(datos_finales, SET_CARTAS)

    except FileNotFoundError as e:
        print(f"\n[ERROR CRÍTICO] Falta un archivo de configuración: {e}")
    except Exception as e:
        print(f"\n[ERROR INESPERADO] {e}")
