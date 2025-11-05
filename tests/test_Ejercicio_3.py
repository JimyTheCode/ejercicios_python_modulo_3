from Ejercicio_3 import crear_contador


def test_contador_incrementa_correctamente():
    contador = crear_contador()
    assert contador() == 1
    assert contador() == 2
    assert contador() == 3


def test_contadores_son_independientes():
    contador1 = crear_contador()
    contador2 = crear_contador()

    assert contador1() == 1
    assert contador1() == 2
    assert contador2() == 1  # independiente
    assert contador1() == 3
    assert contador2() == 2


def test_contador_no_resetea():
    contador = crear_contador()
    for _ in range(5):
        contador()
    assert contador() == 6
