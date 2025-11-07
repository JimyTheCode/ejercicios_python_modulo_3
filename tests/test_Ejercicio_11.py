import os
import pytest
from rich.console import Console

from Ejercicio_11 import agregar_tarea, ver_tareas, ARCHIVO_TAREAS

console = Console()

@pytest.fixture(autouse=True)
def limpiar_archivo():
    """Crea un archivo vacío antes de cada prueba y lo elimina al final."""
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    yield
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)


def test_agregar_tarea_crea_archivo_y_guarda():
    """Verifica que se cree el archivo y se guarde la tarea correctamente."""
    agregar_tarea("Terminar informe")
    assert os.path.exists(ARCHIVO_TAREAS)
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
    assert contenido == "Terminar informe"


def test_ver_tareas_retorna_lista_correcta():
    """Prueba que se lean correctamente las tareas del archivo."""
    tareas_iniciales = ["Tarea 1", "Tarea 2", "Tarea 3"]
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        f.write("\n".join(tareas_iniciales))

    tareas_leidas = ver_tareas()
    assert tareas_leidas == tareas_iniciales


def test_ver_tareas_archivo_vacio():
    """Debe retornar lista vacía si el archivo no existe o está vacío."""
    if os.path.exists(ARCHIVO_TAREAS):
        os.remove(ARCHIVO_TAREAS)
    assert ver_tareas() == []


def test_agregar_varias_tareas():
    """Verifica que varias llamadas agreguen tareas sin borrar las anteriores."""
    agregar_tarea("Comprar pan")
    agregar_tarea("Estudiar Python")
    agregar_tarea("Hacer ejercicio")

    tareas = ver_tareas()
    assert tareas == ["Comprar pan", "Estudiar Python", "Hacer ejercicio"]
    assert len(tareas) == 3


def test_no_agrega_tareas_vacias(monkeypatch):
    """Simula ingreso de tarea vacía (aunque main valida esto, se prueba función directa)."""
    agregar_tarea("  ")
    tareas = ver_tareas()
    assert tareas == []
