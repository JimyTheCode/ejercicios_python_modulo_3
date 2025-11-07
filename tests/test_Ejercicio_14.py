import json
from unittest.mock import mock_open, patch
from Ejercicio_14 import (
    leer_csv,
    leer_json,
    generar_reporte,
    guardar_reporte,
)


# ---------- PRUEBAS PARA leer_csv ----------

def test_leer_csv_exitoso():
    """Debe leer correctamente un archivo CSV válido."""
    csv_data = "id,nombre\n1,Ana\n2,Juan\n"
    with patch("builtins.open", mock_open(read_data=csv_data)):
        resultado = leer_csv("data/estudiantes.csv")

    assert isinstance(resultado, list)
    assert resultado[0]["nombre"] == "Ana"
    assert resultado[1]["id"] == "2"


def test_leer_csv_archivo_no_encontrado(capsys):
    """Debe retornar lista vacía si el archivo CSV no existe."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        resultado = leer_csv("data/no_existe.csv")

    assert resultado == []
    salida = capsys.readouterr().out
    assert " No se encontró el archivo CSV" in salida


# ---------- PRUEBAS PARA leer_json ----------

def test_leer_json_exitoso():
    """Debe leer correctamente un archivo JSON válido."""
    data = {"1": ["Matemáticas", "Historia"]}
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        resultado = leer_json("data/cursos.json")

    assert isinstance(resultado, dict)
    assert resultado["1"] == ["Matemáticas", "Historia"]


def test_leer_json_invalido(capsys):
    """Debe manejar un archivo JSON con formato incorrecto."""
    with patch("builtins.open", mock_open(read_data="no es json válido")):
        resultado = leer_json("data/cursos.json")

    assert resultado == {}
    salida = capsys.readouterr().out
    assert "Error al decodificar" in salida


def test_leer_json_archivo_no_encontrado(capsys):
    """Debe manejar archivo JSON inexistente."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        resultado = leer_json("data/no_existe.json")

    assert resultado == {}
    salida = capsys.readouterr().out
    assert " No se encontró el archivo JSON" in salida


# ---------- PRUEBAS PARA generar_reporte ----------

def test_generar_reporte_exitoso():
    """Debe generar el texto del reporte correctamente."""
    estudiantes = [{"id": "1", "nombre": "Ana"}, {"id": "2", "nombre": "Juan"}]
    cursos = {"1": ["Matemáticas", "Historia"], "2": ["Programación"]}
    reporte = generar_reporte(estudiantes, cursos)

    assert "Ana" in reporte
    assert "Matemáticas" in reporte
    assert "Juan" in reporte
    assert "Programación" in reporte


def test_generar_reporte_sin_cursos():
    """Debe indicar 'Sin cursos registrados' si el estudiante no tiene cursos."""
    estudiantes = [{"id": "1", "nombre": "Ana"}]
    cursos = {}
    reporte = generar_reporte(estudiantes, cursos)

    assert "Sin cursos registrados" in reporte


def test_guardar_reporte_exitoso(tmp_path):
    """Debe crear un archivo con el contenido del reporte."""
    contenido = "Ejemplo de reporte"
    archivo = tmp_path / "reporte.txt"
    guardar_reporte(str(archivo), contenido)

    with open(archivo, "r", encoding="utf-8") as f:
        data = f.read()
    assert "Ejemplo de reporte" in data
