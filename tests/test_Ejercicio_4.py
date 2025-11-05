import pytest
from Ejercicio_4 import aplicar_validador, es_email_valido, es_mayor_a_10


def test_es_email_valido():
    assert es_email_valido("usuario@test.com")
    assert es_email_valido("nombre.apellido@dominio.co")
    assert not es_email_valido("sin_arroba.com")
    assert not es_email_valido("usuario@.com")


def test_es_mayor_a_10():
    assert es_mayor_a_10(11)
    assert not es_mayor_a_10(10)
    assert not es_mayor_a_10(3)


def test_aplicar_validador_con_emails():
    datos = ["a@a.com", "b@", "c@c.net"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == ["a@a.com", "c@c.net"]


def test_aplicar_validador_con_numeros():
    datos = [5, 12, 8, 20]
    resultado = aplicar_validador(datos, es_mayor_a_10)
    assert resultado == [12, 20]


def test_aplicar_validador_error_si_no_funcion():
    with pytest.raises(TypeError):
        aplicar_validador([1, 2, 3], "no_es_funcion")
