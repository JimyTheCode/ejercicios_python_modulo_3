from Ejercicio_7 import filtrar_aprobados


def test_filtrar_aprobados_exitoso():
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("María", 3.9)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == [("Ana", 4.5), ("María", 3.9)]


def test_filtrar_aprobados_vacio():
    estudiantes = [("Luis", 2.5), ("Sofía", 1.9)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == []


def test_filtrar_aprobados_todos_aprueban():
    estudiantes = [("Carlos", 3.0), ("Laura", 3.5)]
    resultado = filtrar_aprobados(estudiantes)
    assert resultado == estudiantes
