import json
from pathlib import Path
import pytest
from rich.console import Console

from Ejercicio_15 import (
    cargar_biblioteca,
    agregar_libro,
    eliminar_libro,
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
    crear_tabla_libros,
)


def escribir_biblioteca(path: Path, lista):
    """Crea o sobrescribe el archivo JSON con la lista de libros."""
    path.write_text(json.dumps(lista, ensure_ascii=False, indent=2), encoding="utf-8")


def test_cargar_biblioteca_no_existe(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    assert not ruta.exists()
    libros = cargar_biblioteca(str(ruta))
    assert libros == []


def test_guardar_y_cargar(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "autor": "García Márquez", "prestado_a": None}
    ]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    assert len(libros) == 1
    assert libros[0]["titulo"] == "Cien Años de Soledad"


def test_agregar_libro_y_persistencia(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    libros = []
    nuevo = agregar_libro(libros, "Nuevo Libro", "Autor X", ruta=str(ruta))
    assert nuevo["libro_id"] == "001"
    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert data[0]["titulo"] == "Nuevo Libro"


def test_eliminar_libro(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [
        {"libro_id": "001", "titulo": "A", "autor": None, "prestado_a": None},
        {"libro_id": "002", "titulo": "B", "autor": None, "prestado_a": None},
    ]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    eliminado = eliminar_libro(libros, "001", ruta=str(ruta))
    assert eliminado["libro_id"] == "001"
    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert len(data) == 1
    assert data[0]["libro_id"] == "002"


def test_prestar_y_devolver_libro(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [{"libro_id": "001", "titulo": "Libro A", "autor": None, "prestado_a": None}]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))

    actualizado = prestar_libro(libros, "001", "María", ruta=str(ruta))
    assert actualizado["prestado_a"] == "María"

    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert data[0]["prestado_a"] == "María"

    devuelto = devolver_libro(libros, "001", ruta=str(ruta))
    assert devuelto["prestado_a"] is None

    data2 = json.loads(ruta.read_text(encoding="utf-8"))
    assert data2[0]["prestado_a"] is None


def test_prestar_ya_prestado_raises(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [{"libro_id": "001", "titulo": "Libro A", "autor": None, "prestado_a": "Pedro"}]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    with pytest.raises(ValueError):
        prestar_libro(libros, "001", "Ana", ruta=str(ruta))


def test_devolver_no_prestado_raises(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [{"libro_id": "001", "titulo": "Libro A", "autor": None, "prestado_a": None}]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    with pytest.raises(ValueError):
        devolver_libro(libros, "001", ruta=str(ruta))


def test_buscar_libro_case_insensitive(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [
        {"libro_id": "001", "titulo": "Python Avanzado", "autor": None, "prestado_a": None},
        {"libro_id": "002", "titulo": "Introducción a PYTHON", "autor": None, "prestado_a": None},
        {"libro_id": "003", "titulo": "Otra Cosa", "autor": None, "prestado_a": None},
    ]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    resultados = buscar_libro(libros, "python")
    assert len(resultados) == 2
    ids = {r["libro_id"] for r in resultados}
    assert ids == {"001", "002"}


def test_ver_libros_prestados(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [
        {"libro_id": "001", "titulo": "A", "autor": None, "prestado_a": "Ana"},
        {"libro_id": "002", "titulo": "B", "autor": None, "prestado_a": None},
    ]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    prestados = ver_libros_prestados(libros)
    assert len(prestados) == 1
    assert prestados[0]["libro_id"] == "001"


def test_crear_tabla_libros_render(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    lista = [
        {"libro_id": "001", "titulo": "A", "autor": "X", "prestado_a": None},
    ]
    escribir_biblioteca(ruta, lista)
    libros = cargar_biblioteca(str(ruta))
    tabla = crear_tabla_libros(libros)

    console = Console(record=True)
    console.print(tabla)
    texto = console.export_text()

    assert "A" in texto
    assert "001" in texto
