from typing import List, Dict
from rich.console import Console
from rich.table import Table


def obtener_palabras_mayusculas(texto: str) -> List[str]:
    """
    Obtiene las palabras con más de 5 letras en mayúsculas desde un texto.

    Args:
        texto (str): Texto de entrada del cual se extraerán las palabras.

    Returns:
        List[str]: Lista de palabras en mayúsculas con más de 5 letras.
    """
    palabras = texto.split()
    return [palabra.upper() for palabra in palabras if len(palabra) > 5]


def crear_diccionario_longitudes(palabras: List[str]) -> Dict[str, int]:
    """
    Crea un diccionario con la longitud de cada palabra.

    Args:
        palabras (List[str]): Lista de palabras en mayúsculas.

    Returns:
        Dict[str, int]: Diccionario con la palabra como clave y su longitud como valor.
    """
    return {palabra: len(palabra) for palabra in palabras}


def mostrar_tabla_resultados(palabras: List[str], longitudes: Dict[str, int]) -> None:
    """
    Muestra los resultados en una tabla formateada usando rich.

    Args:
        palabras (List[str]): Lista de palabras en mayúsculas.
        longitudes (Dict[str, int]): Diccionario con las longitudes de cada palabra.

    Returns:
        None
    """
    console = Console()
    tabla = Table(title="🔠 Palabras con más de 5 letras", show_lines=True)
    tabla.add_column("Palabra", style="cyan", justify="center")
    tabla.add_column("Longitud", style="green", justify="center")

    for palabra in palabras:
        tabla.add_row(palabra, str(longitudes[palabra]))

    console.print(tabla)


if __name__ == "__main__":
    texto = (
        "La programación en Python permite resolver problemas complejos "
        "de manera eficiente y elegante utilizando estructuras poderosas."
    )

    palabras_filtradas = obtener_palabras_mayusculas(texto)
    diccionario_longitudes = crear_diccionario_longitudes(palabras_filtradas)
    mostrar_tabla_resultados(palabras_filtradas, diccionario_longitudes)
