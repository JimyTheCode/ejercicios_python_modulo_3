from Ejercicio_9 import sumar_lista, concatenar_textos


def test_sumar_lista_exitoso():
    numeros = [1, 2, 3, 4, 5]
    resultado = sumar_lista(numeros)
    assert resultado == 15


def test_sumar_lista_con_negativos():
    numeros = [10, -5, 3]
    resultado = sumar_lista(numeros)
    assert resultado == 8


def test_concatenar_textos_exitoso():
    textos = ["Hola", " ", "SENA", "!"]
    resultado = concatenar_textos(textos)
    assert resultado == "Hola SENA!"


def test_concatenar_textos_vacio():
    textos = [""]
    resultado = concatenar_textos(textos)
    assert resultado == ""
