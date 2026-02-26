def generar_tablero():
    """
    Retorna una lista de diccionarios representando las 40 casillas.
    Basado en los precios y nombres de la edición estándar.
    """
    tablero = [
        {"nombre": "Salida", "tipo": "especial"},
        {"nombre": "Avenida Mediterráneo", "tipo": "propiedad", "grupo": "marrón", "precio": 60, "renta": 2},
        {"nombre": "Arca Comunal 1", "tipo": "arca"},
        {"nombre": "Avenida Báltica", "tipo": "propiedad", "grupo": "marrón", "precio": 60, "renta": 4},
        {"nombre": "Impuesto sobre Ingresos", "tipo": "impuesto", "costo": 200},
        {"nombre": "Ferrocarril Reading", "tipo": "estacion", "precio": 200, "renta_base": 25},
        {"nombre": "Avenida Oriental", "tipo": "propiedad", "grupo": "celeste", "precio": 100, "renta": 6},
        {"nombre": "Suerte 1", "tipo": "suerte"},
        {"nombre": "Avenida Vermont", "tipo": "propiedad", "grupo": "celeste", "precio": 100, "renta": 6},
        {"nombre": "Avenida Connecticut", "tipo": "propiedad", "grupo": "celeste", "precio": 120, "renta": 8},
        {"nombre": "Cárcel / Solo Visitas", "tipo": "especial"},
        {"nombre": "Plaza San Carlos", "tipo": "propiedad", "grupo": "rosa", "precio": 140, "renta": 10},
        {"nombre": "Compañía de Electricidad", "tipo": "servicio", "precio": 150},
        {"nombre": "Avenida Estados", "tipo": "propiedad", "grupo": "rosa", "precio": 140, "renta": 10},
        {"nombre": "Avenida Virginia", "tipo": "propiedad", "grupo": "rosa", "precio": 160, "renta": 12},
        {"nombre": "Ferrocarril de Pensilvania", "tipo": "estacion", "precio": 200, "renta_base": 25},
        {"nombre": "Plaza Santiago", "tipo": "propiedad", "grupo": "naranja", "precio": 180, "renta": 14},
        {"nombre": "Arca Comunal 2", "tipo": "arca"},
        {"nombre": "Avenida Tennessee", "tipo": "propiedad", "grupo": "naranja", "precio": 180, "renta": 14},
        {"nombre": "Avenida Nueva York", "tipo": "propiedad", "grupo": "naranja", "precio": 200, "renta": 16},
        {"nombre": "Parada Libre", "tipo": "especial"},
        {"nombre": "Avenida Kentucky", "tipo": "propiedad", "grupo": "rojo", "precio": 220, "renta": 18},
        {"nombre": "Suerte 2", "tipo": "suerte"},
        {"nombre": "Avenida Indiana", "tipo": "propiedad", "grupo": "rojo", "precio": 220, "renta": 18},
        {"nombre": "Avenida Illinois", "tipo": "propiedad", "grupo": "rojo", "precio": 240, "renta": 20},
        {"nombre": "Ferrocarril B. & O.", "tipo": "estacion", "precio": 200, "renta_base": 25},
        {"nombre": "Avenida Atlántico", "tipo": "propiedad", "grupo": "amarillo", "precio": 260, "renta": 22},
        {"nombre": "Avenida Ventnor", "tipo": "propiedad", "grupo": "amarillo", "precio": 260, "renta": 22},
        {"nombre": "Obras de Agua Potable", "tipo": "servicio", "precio": 150},
        {"nombre": "Jardines Marvin", "tipo": "propiedad", "grupo": "amarillo", "precio": 280, "renta": 24},
        {"nombre": "Váyase a la Cárcel", "tipo": "especial"},
        {"nombre": "Avenida Pacífico", "tipo": "propiedad", "grupo": "verde", "precio": 300, "renta": 26},
        {"nombre": "Avenida Carolina del Norte", "tipo": "propiedad", "grupo": "verde", "precio": 300, "renta": 26},
        {"nombre": "Arca Comunal 3", "tipo": "arca"},
        {"nombre": "Avenida Pensilvania", "tipo": "propiedad", "grupo": "verde", "precio": 320, "renta": 28},
        {"nombre": "Ferrocarril Short Line", "tipo": "estacion", "precio": 200, "renta_base": 25},
        {"nombre": "Suerte 3", "tipo": "suerte"},
        {"nombre": "Plaza Parque", "tipo": "propiedad", "grupo": "azul", "precio": 350, "renta": 35},
        {"nombre": "Impuesto de Lujo", "tipo": "impuesto", "costo": 100},
        {"nombre": "Paseo Tablado", "tipo": "propiedad", "grupo": "azul", "precio": 400, "renta": 50}
    ]
    return tablero


