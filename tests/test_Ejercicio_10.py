from Ejercicio_10 import explorar_estructura


def test_explorar_lista_simple():
    datos = [1, 2, 3]
    resultado = explorar_estructura(datos)
    assert resultado == [(1, 2), (2, 2), (3, 2)]


def test_explorar_diccionario_anidado():
    datos = {"a": 1, "b": {"c": 2}}
    resultado = explorar_estructura(datos)
    assert (1, 2) in resultado
    assert (2, 3) in resultado


def test_explorar_mixto():
    datos = [1, [2, 3], {"x": 4}]
    resultado = explorar_estructura(datos)
    valores = [v for v, _ in resultado]
    assert set(valores) == {1, 2, 3, 4}


def test_explorar_valor_unico():
    datos = 10
    resultado = explorar_estructura(datos)
    assert resultado == [(10, 1)]
