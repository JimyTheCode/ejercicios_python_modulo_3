from typing import Any
from rich.console import Console
from rich.table import Table


def explorar_estructura(elemento: Any, profundidad: int = 1) -> list[tuple[Any, int]]:
    """
    Explora recursivamente cualquier estructura de datos (listas, diccionarios, etc.)
    e identifica los valores no iterables junto a su nivel de profundidad.

    Args:
        elemento (Any): Estructura de datos a explorar (puede contener listas, tuplas, dict, etc.).
        profundidad (int, optional): Nivel actual de profundidad. Por defecto es 1.

    Returns:
        list[tuple[Any, int]]: Lista de tuplas con cada valor no iterable y su profundidad.
    """
    resultados: list[tuple[Any, int]] = []

    # Caso base: si el elemento no es iterable (string, número, etc.)
    if isinstance(elemento, (str, int, float, bool)) or elemento is None:
        resultados.append((elemento, profundidad))
        return resultados

    # Si es un diccionario, exploramos sus valores
    if isinstance(elemento, dict):
        for valor in elemento.values():
            resultados.extend(explorar_estructura(valor, profundidad + 1))

    # Si es una lista, tupla o conjunto, exploramos sus elementos
    elif isinstance(elemento, (list, tuple, set)):
        for sub_elemento in elemento:
            resultados.extend(explorar_estructura(sub_elemento, profundidad + 1))

    # Cualquier otro tipo de objeto (caso residual)
    else:
        resultados.append((repr(elemento), profundidad))

    return resultados


def mostrar_tabla_resultados(resultados: list[tuple[Any, int]]) -> None:
    """
    Muestra los valores y su profundidad en una tabla usando la librería rich.

    Args:
        resultados (list[tuple[Any, int]]): Lista de tuplas con valores y profundidad.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="🔍 Explorador de Estructuras de Datos", show_lines=True)
    tabla.add_column("Valor", style="cyan", justify="center")
    tabla.add_column("Profundidad", style="green", justify="center")

    for valor, nivel in resultados:
        tabla.add_row(str(valor), str(nivel))

    console.print(tabla)


if __name__ == "__main__":
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    resultados = explorar_estructura(estructura)
    mostrar_tabla_resultados(resultados)
