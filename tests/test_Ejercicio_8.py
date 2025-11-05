from Ejercicio_8 import obtener_palabras_mayusculas, crear_diccionario_longitudes


def test_obtener_palabras_mayusculas_exitoso():
    texto = "Python es un lenguaje de programación increíble"
    resultado = obtener_palabras_mayusculas(texto)
    assert resultado == ["PYTHON", "LENGUAJE", "PROGRAMACIÓN", "INCREÍBLE"]


def test_obtener_palabras_mayusculas_vacio():
    texto = "Hola soy yo"
    resultado = obtener_palabras_mayusculas(texto)
    assert resultado == []


def test_crear_diccionario_longitudes():
    palabras = ["PYTHON", "EJEMPLO"]
    resultado = crear_diccionario_longitudes(palabras)
    assert resultado == {"PYTHON": 6, "EJEMPLO": 7}
