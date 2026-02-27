# 🎩 Pynche-Mono v2.0: Monte Carlo Monopoly Framework
**Un Laboratorio de Teoría de Juegos, Alineamientos de Rol y Análisis Estocástico**

`Pynche-Mono` es una plataforma de simulación avanzada desarrollada en Python para el análisis del Monopoly. A diferencia de un simulador de juego convencional, este framework permite la experimentación masiva mediante el método de Monte Carlo, permitiendo evaluar cómo diversas "alineaciones" (basadas en la matriz de D&D) y configuraciones de mazos alteran la probabilidad de aterrizaje y la solvencia económica de los jugadores.

---

##  Arquitectura del Sistema

El proyecto sigue un diseño modular para separar la definición de datos de la lógica de ejecución:

###  Organización de Directorios
* **`configs/`**: El "Cerebro" del sistema. Contiene archivos YAML que definen los escenarios (Steering Files).
* **`data/`**:
    * `card_sets/`: Definiciones JSON de mazos de Suerte y Arca Comunal.
    * `resultados/`: Almacén de archivos CSV generados tras cada ejecución.
* **`src/`**:
    * `models/jugador.py`: Entidad que gestiona saldo, posición, inventario de propiedades y estado de quiebra.
    * `logic/`:
        * `tablero.py`: Fuente de verdad geográfica con precios, rentas y tipos de casillas.
        * `dados.py`: Generador de números aleatorios con soporte para semillas y dobles.
        * `cartas.py`: Lógica de carga y barajado de mazos.
    * **`engine.py`**: El motor orquestador. Maneja el flujo de turnos, transacciones económicas y resolución de eventos.
* **`main.py`**: Interfaz de Línea de Comandos (CLI) que conecta los Steering Files con el motor.

---

##  Alineamientos D&D (Escenarios de Prueba)

El framework utiliza la matriz de alineamiento de D&D para definir la "personalidad" de la simulación mediante los Steering Files:

| Alineamiento | Comportamiento del Escenario | Impacto Típico |
| :--- | :--- | :--- |
| **Legal-Bueno** | Alta liquidez, cobro de salida elevado y mazos benévolos. | Alta supervivencia, baja volatilidad. |
| **Neutral-Auténtico** | Configuración estándar basada en las reglas oficiales. | El "Baseline" estadístico para comparaciones. |
| **Caótico-Malvado** | Rentas predatorias, mazos con alta frecuencia de cárcel y escasez de oro. | Quiebras masivas, alta frecuencia en casilla 10. |

---

##  Especificaciones del Motor Económico

El motor ha sido actualizado para procesar transferencias reales de capital entre entidades:

1.  **Mecánica de Compra**: Si un jugador aterriza en una propiedad sin dueño, se verifica su saldo contra el precio definido en `tablero.py`. Si es solvente, el motor actualiza el diccionario de la casilla asignando al jugador como propietario.
2.  **Mecánica de Renta**: Al caer en propiedad ajena, el motor ejecuta `jugador.pagar(renta, destinatario=dueno)`, transfiriendo los fondos directamente entre objetos.
3.  **Gestión de Quiebra**: Un jugador es marcado como `esta_quebrado = True` si su saldo es insuficiente para cubrir una deuda, transfiriendo su capital remanente al acreedor antes de ser retirado de la simulación.

---

##  Interfaz de Comandos (CLI)

El archivo `main.py` permite una manipulación dinámica del experimento sin modificar archivos internos:

python main.py [FLAGS]


Argumentos Soportados:
-c, --config: Nombre del archivo YAML en configs/ (ej: caotico_malvado).

-t, --turnos: Sobrescribe la duración (ej: -t 1000 para crónicas rápidas).

-s, --seed: Define la semilla aleatoria para garantizar reproducibilidad.

-v, --verbosity: Controla el flujo de salida:

    0: Ejecución silenciosa (máxima velocidad).
    1: Resumen ejecutivo y Reporte de Supervivencia.
    2: Notificaciones de compras, rentas y aterrizajes.
    3: Debug total (dados, cartas y balances por turno).

** Reporte de Supervivencia y Datos
Al concluir cada simulación, el framework genera un reporte dual:

    *Reporte de Supervivencia: Una crónica en consola que detalla quién sobrevivió, quién quebró y el balance de oro final de cada "aventurero".

    *Dataset CSV: Un archivo detallado con la frecuencia de visitas por casilla y la probabilidad porcentual calculada, ideal para su posterior análisis en herramientas de Data Science.

