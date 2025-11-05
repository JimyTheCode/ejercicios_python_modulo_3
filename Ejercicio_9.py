from functools import reduce
from typing import List
from rich.console import Console
from rich.table import Table


def sumar_lista(numeros: List[int]) -> int:
    """
    Calcula la suma total de una lista de números usando reduce.

    Args:
        numeros (List[int]): Lista de números enteros a sumar.

    Returns:
        int: Resultado de la suma total.
    """
    return reduce(lambda x, y: x + y, numeros)


def concatenar_textos(textos: List[str]) -> str:
    """
    Concatena una lista de strings en una sola cadena usando reduce.

    Args:
        textos (List[str]): Lista de cadenas de texto.

    Returns:
        str: Texto concatenado resultante.
    """
    return reduce(lambda a, b: a + b, textos)


def mostrar_resultados(suma_total: int, frase: str) -> None:
    """
    Muestra los resultados en una tabla formateada usando rich.

    Args:
        suma_total (int): Resultado de la suma total.
        frase (str): Frase concatenada.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="🧮 Resultados con reduce", show_lines=True)
    tabla.add_column("Operación", style="cyan", justify="center")
    tabla.add_column("Resultado", style="green", justify="center")

    tabla.add_row("Suma total de la lista [1, 2, 3, 4, 5]", str(suma_total))
    tabla.add_row("Concatenación de textos", frase)

    console.print(tabla)


if __name__ == "__main__":
    lista_numeros = [1, 2, 3, 4, 5]
    lista_textos = ["Hola", " ", "SENA", "!"]

    total = sumar_lista(lista_numeros)
    frase_final = concatenar_textos(lista_textos)
    mostrar_resultados(total, frase_final)
