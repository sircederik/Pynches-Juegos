# Pynche-Mono
**Framework de Simulación Monte Carlo para el Análisis de Monopoly**

`Pynche-Mono` es una plataforma de experimentación diseñada para modelar, simular y analizar el comportamiento estocástico del juego de Monopoly. A diferencia de un simulador rígido, este proyecto nace con la filosofía de **configurabilidad total**, permitiendo a investigadores y entusiastas de la teoría de juegos explorar cómo pequeñas variaciones en las reglas o el azar alteran la economía del tablero.

## Objetivo del Proyecto
El sistema busca ser un laboratorio virtual donde el usuario pueda responder preguntas complejas mediante el análisis de datos masivos:
* ¿Cómo cambia la rentabilidad de los bloques de color si modifico el mazo de cartas?
* ¿Qué impacto tiene en la probabilidad de quiebra una semilla de azar específica?
* ¿Cuál es la convergencia estadística tras un volumen masivo de iteraciones?

## Alta Configurabilidad
El diseño modular permite intervenir en cada capa del simulador sin necesidad de reescribir el motor principal:

* **Escenarios de Cartas (Card Sets):** Mediante archivos **JSON**, el usuario puede definir sus propios paquetes de cartas (oficiales, agresivos, de alta inflación o personalizados), alterando las probabilidades de movimiento y flujo de efectivo.
* **Volumen de Datos:** La duración de la simulación es **definida por el usuario**, permitiendo desde pruebas rápidas de integridad hasta ejecuciones masivas de alto rendimiento para alcanzar el estado estacionario.
* **Control de Azar:** Implementación de semillas mediante `numpy.random.Generator` para garantizar la **reproducibilidad total** de cualquier escenario diseñado.
* **Arquitectura Desacoplada:** Estructura que separa claramente los modelos de datos de la lógica de negocio, facilitando la extensión del código.

## Estructura del Repositorio
```text
Pynche-Mono/
├── data/
│   ├── card_sets/          # Repositorio de paquetes de cartas configurables (JSON)
│   └── resultados/         # Dataset generado (CSVs) para análisis posterior
├── src/
│   ├── logic/              # Reglas dinámicas (dados, tablero, cartas)
│   ├── models/             # Entidades de datos (jugador)
│   └── engine.py           # Intérprete de reglas y orquestador de turnos
├── main.py                 # Interfaz de configuración del experimento
└── README.md
