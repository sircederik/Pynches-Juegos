def generar_tablero():
    """
    Retorna una lista de diccionarios representando las 40 casillas.
    Incluye la clave 'dueno' inicializada en None para la lógica económica.
    """
    tablero = [
        {"nombre": "Salida", "tipo": "especial"},
        {"nombre": "Avenida Mediterráneo", "tipo": "calle", "grupo": "marrón", "precio": 60, "renta": 2, "dueno": None},
        {"nombre": "Arca Comunal 1", "tipo": "arca"},
        {"nombre": "Avenida Báltica", "tipo": "calle", "grupo": "marrón", "precio": 60, "renta": 4, "dueno": None},
        {"nombre": "Impuesto sobre Ingresos", "tipo": "impuesto", "costo": 200},
        {"nombre": "Ferrocarril Reading", "tipo": "ferrocarril", "precio": 200, "renta": 25, "dueno": None},
        {"nombre": "Avenida Oriental", "tipo": "calle", "grupo": "celeste", "precio": 100, "renta": 6, "dueno": None},
        {"nombre": "Suerte 1", "tipo": "suerte"},
        {"nombre": "Avenida Vermont", "tipo": "calle", "grupo": "celeste", "precio": 100, "renta": 6, "dueno": None},
        {"nombre": "Avenida Connecticut", "tipo": "calle", "grupo": "celeste", "precio": 120, "renta": 8, "dueno": None},
        {"nombre": "Cárcel / Solo Visitas", "tipo": "especial"},
        {"nombre": "Plaza San Carlos", "tipo": "calle", "grupo": "rosa", "precio": 140, "renta": 10, "dueno": None},
        {"nombre": "Compañía de Electricidad", "tipo": "servicio", "precio": 150, "renta": 10, "dueno": None},
        {"nombre": "Avenida Estados", "tipo": "calle", "grupo": "rosa", "precio": 140, "renta": 10, "dueno": None},
        {"nombre": "Avenida Virginia", "tipo": "calle", "grupo": "rosa", "precio": 160, "renta": 12, "dueno": None},
        {"nombre": "Ferrocarril de Pensilvania", "tipo": "ferrocarril", "precio": 200, "renta": 25, "dueno": None},
        {"nombre": "Plaza Santiago", "tipo": "calle", "grupo": "naranja", "precio": 180, "renta": 14, "dueno": None},
        {"nombre": "Arca Comunal 2", "tipo": "arca"},
        {"nombre": "Avenida Tennessee", "tipo": "calle", "grupo": "naranja", "precio": 180, "renta": 14, "dueno": None},
        {"nombre": "Avenida Nueva York", "tipo": "calle", "grupo": "naranja", "precio": 200, "renta": 16, "dueno": None},
        {"nombre": "Parada Libre", "tipo": "especial"},
        {"nombre": "Avenida Kentucky", "tipo": "calle", "grupo": "rojo", "precio": 220, "renta": 18, "dueno": None},
        {"nombre": "Suerte 2", "tipo": "suerte"},
        {"nombre": "Avenida Indiana", "tipo": "calle", "grupo": "rojo", "precio": 220, "renta": 18, "dueno": None},
        {"nombre": "Avenida Illinois", "tipo": "calle", "grupo": "rojo", "precio": 240, "renta": 20, "dueno": None},
        {"nombre": "Ferrocarril B. & O.", "tipo": "ferrocarril", "precio": 200, "renta": 25, "dueno": None},
        {"nombre": "Avenida Atlántico", "tipo": "calle", "grupo": "amarillo", "precio": 260, "renta": 22, "dueno": None},
        {"nombre": "Avenida Ventnor", "tipo": "calle", "grupo": "amarillo", "precio": 260, "renta": 22, "dueno": None},
        {"nombre": "Obras de Agua Potable", "tipo": "servicio", "precio": 150, "renta": 10, "dueno": None},
        {"nombre": "Jardines Marvin", "tipo": "calle", "grupo": "amarillo", "precio": 280, "renta": 24, "dueno": None},
        {"nombre": "Váyase a la Cárcel", "tipo": "especial"},
        {"nombre": "Avenida Pacífico", "tipo": "calle", "grupo": "verde", "precio": 300, "renta": 26, "dueno": None},
        {"nombre": "Avenida Carolina del Norte", "tipo": "calle", "grupo": "verde", "precio": 300, "renta": 26, "dueno": None},
        {"nombre": "Arca Comunal 3", "tipo": "arca"},
        {"nombre": "Avenida Pensilvania", "tipo": "calle", "grupo": "verde", "precio": 320, "renta": 28, "dueno": None},
        {"nombre": "Ferrocarril Short Line", "tipo": "ferrocarril", "precio": 200, "renta": 25, "dueno": None},
        {"nombre": "Suerte 3", "tipo": "suerte"},
        {"nombre": "Plaza Parque", "tipo": "calle", "grupo": "azul", "precio": 350, "renta": 35, "dueno": None},
        {"nombre": "Impuesto de Lujo", "tipo": "impuesto", "costo": 100},
        {"nombre": "Muelle", "tipo": "calle", "grupo": "azul", "precio": 400, "renta": 50, "dueno": None}
    ]
    return tablero
