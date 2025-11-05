import pytest
from Ejercicio_2 import crear_perfil


def test_crear_perfil_basico():
    perfil = crear_perfil("Ana", 30)
    assert "Ana" in perfil
    assert "30 años" in perfil
    assert "No especificados" in perfil
    assert "No registradas" in perfil


def test_crear_perfil_con_hobbies_y_redes():
    perfil = crear_perfil("Luis", 22, "correr", "leer", twitter="@luisito", instagram="@lu_22")
    assert "correr" in perfil
    assert "leer" in perfil
    assert "twitter: @luisito" in perfil
    assert "instagram: @lu_22" in perfil


def test_crear_perfil_nombre_invalido():
    with pytest.raises(ValueError, match="nombre no puede estar vacío"):
        crear_perfil("", 25)


def test_crear_perfil_edad_invalida():
    with pytest.raises(ValueError, match="edad debe ser mayor que 0"):
        crear_perfil("Juan", 0)
