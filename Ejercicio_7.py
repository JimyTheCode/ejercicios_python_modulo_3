from typing import List, Tuple
from rich.console import Console
from rich.table import Table


def filtrar_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra los estudiantes que aprobaron con nota mayor o igual a 3.0.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas con nombre y nota del estudiante.

    Returns:
        List[Tuple[str, float]]: Nueva lista con solo los estudiantes que aprobaron.
    """
    return list(filter(lambda est: est[1] >= 3.0, estudiantes))


def mostrar_tabla_estudiantes(estudiantes: List[Tuple[str, float]]) -> None:
    """
    Muestra una tabla con los estudiantes y sus notas usando la librería rich.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas con nombre y nota del estudiante.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="📘 Estudiantes Aprobados", show_lines=True)
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Nota", style="green", justify="center")

    for nombre, nota in estudiantes:
        tabla.add_row(nombre, f"{nota:.1f}")

    console.print(tabla)


if __name__ == "__main__":
    estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("María", 3.9)]
    aprobados = filtrar_aprobados(estudiantes)
    mostrar_tabla_estudiantes(aprobados)
