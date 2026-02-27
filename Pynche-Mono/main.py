import os
import yaml
import argparse
import pandas as pd
from src.models.jugador import Jugador
from src.logic.dados import Dados
from src.logic.tablero import generar_tablero
from src.logic.cartas import cargar_paquete_de_cartas # La nueva función
from src.engine import MonopolyEngine

def cargar_configuracion():
    """Busca el archivo YAML en la carpeta configs/ y permite sobrescritura."""
    parser = argparse.ArgumentParser(description="Pynche-Mono Steering System")
    parser.add_argument("-c", "--config", default="default", help="Nombre del archivo en configs/ (sin .yaml)")
    parser.add_argument("-t", "--turnos", type=int, help="Sobrescribir cantidad de turnos")
    parser.add_argument("-s", "--seed", type=int, help="Sobrescribir semilla")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2, 3], 
                        help="Nivel de verbosidad (0: Silent, 1: Normal, 2: Detailed, 3: Debug)")
    args = parser.parse_args()

    # Construir ruta: si el usuario pone 'oficial', buscamos 'configs/oficial.yaml'
    nombre_archivo = args.config if args.config.endswith(".yaml") else f"{args.config}.yaml"
    ruta_config = os.path.join("configs", nombre_archivo)

    if not os.path.exists(ruta_config):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_config}")

    with open(ruta_config, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Inyección de parámetros desde CLI (Línea de comandos)
    if args.turnos: config['simulation_params']['turnos'] = args.turnos
    if args.seed: config['simulation_params']['semilla'] = args.seed
    if args.verbosity is not None: # El 0 es evaluado como False, por eso usamos 'is not None'
        config['output_params']['verbosity'] = args.verbosity
    return config

def ejecutar_simulacion(config):
    s_params = config['simulation_params']
    r_params = config['rules_configuration']

    # Extraer verbosidad (por defecto 1 si no existe)
    v_level = config['output_params'].get('verbosity', 1)

    print(f"\n>>> Lanzando Experimento: {config['experiment_name']}")

    # Iniciar componentes con los datos del Steering File
    dados = Dados(semilla=s_params['semilla'])
    tablero = generar_tablero()
    m_suerte, m_arca = cargar_paquete_de_cartas(r_params['set_cartas'], dados.rng)
    cobro_salida = r_params.get('cobro_salida',200)

    # Configurar jugadores
    jugadores = [Jugador(i, f"J_{i}") for i in range(1, s_params['num_jugadores'] + 1)]
    for j in jugadores:
        j.dinero = r_params.get('dinero_inicial', 1500)

    # Ejecutar Motor
    engine = MonopolyEngine(jugadores, tablero, m_suerte, m_arca, dados, cobro_salida, verbosity=v_level)
    engine.ejecutar_partida(max_turnos=s_params['turnos'])

    # Consolidar resultados
    visitas = [0] * 40
    for j in jugadores:
        for i in range(40):
            visitas[i] += j.contador_visitas[i]

    return visitas, jugadores

def reporte_supervivencia(jugadores):
    print("\n" + "="*40)
    print("ESTADO FINAL DE LOS AVENTUREROS")
    print("="*40)
    for j in jugadores:
        estado = "QUEBRADO 💀" if j.esta_quebrado else "ACTIVO 💰"
        print(f"{j.nombre:<10} | {estado} | Balance: ${j.dinero}")
    print("="*40)

def guardar_reporte(visitas, config):
    o_params = config['output_params']
    if not os.path.exists(o_params['output_dir']):
        os.makedirs(o_params['output_dir'])

    tablero = generar_tablero()
    df = pd.DataFrame({
        "Casilla": [c["nombre"] for c in tablero],
        "Visitas": visitas
    })
    df["Probabilidad (%)"] = (df["Visitas"] / df["Visitas"].sum()) * 100

    archivo_csv = os.path.join(o_params['output_dir'], f"{config['experiment_name']}.csv")
    df.to_csv(archivo_csv, index=False)

    print(f"\n[DATOS] Reporte generado en: {archivo_csv}")

    if o_params.get('verbose_summary'):
        print("\n--- TOP 10 CASILLAS ---")
        print(df.sort_values("Visitas", ascending=False).head(10).to_string(index=False))

if __name__ == "__main__":
    try:
        cfg = cargar_configuracion()
        res, jugadores = ejecutar_simulacion(cfg)
        reporte_supervivencia(jugadores)
        guardar_reporte(res, cfg)
    except Exception as e:
        print(f"\n[ERROR] Hubo un problema: {e}")
