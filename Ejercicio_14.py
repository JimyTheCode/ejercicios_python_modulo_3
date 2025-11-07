"""
Ejercicio 14: Generador de Reportes a partir de Múltiples Archivos

"""

import csv
import json
import os
from typing import List, Dict, Any
from rich.console import Console
from rich.panel import Panel

console = Console()


def leer_csv(nombre_archivo: str) -> List[Dict[str, str]]:
    """
    Lee un archivo CSV y devuelve una lista de diccionarios.

    Args:
        nombre_archivo (str): Ruta al archivo CSV.

    Returns:
        List[Dict[str, str]]: Lista de diccionarios con los datos del archivo.
    """
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        console.print(f"[red] No se encontró el archivo CSV: {nombre_archivo}[/red]")
        return []


def leer_json(nombre_archivo: str) -> Dict[str, Any]:
    """
    Lee un archivo JSON y devuelve un diccionario con su contenido.

    Args:
        nombre_archivo (str): Ruta al archivo JSON.

    Returns:
        Dict[str, Any]: Diccionario con los datos del archivo JSON.
    """
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        console.print(f"[red] No se encontró el archivo JSON: {nombre_archivo}[/red]")
        return {}
    except json.JSONDecodeError:
        console.print(f"[red] Error al decodificar el archivo JSON: {nombre_archivo}[/red]")
        return {}


def generar_reporte(estudiantes: List[Dict[str, str]], cursos: Dict[str, Any]) -> str:
    """
    Combina la información de estudiantes y cursos en un reporte de texto.

    Args:
        estudiantes (List[Dict[str, str]]): Lista de estudiantes con id y nombre.
        cursos (Dict[str, Any]): Diccionario con id de estudiante y lista de cursos.

    Returns:
        str: Texto del reporte generado.
    """
    if not estudiantes:
        return " No hay datos de estudiantes para generar el reporte."

    reporte = ""
    for est in estudiantes:
        cursos_est = cursos.get(est["id"], ["Sin cursos registrados"])
        lista_cursos = ", ".join(cursos_est)
        reporte += f"Estudiante: {est['nombre']}\nCursos: {lista_cursos}\n\n"
    return reporte.strip()


def guardar_reporte(nombre_archivo: str, contenido: str) -> None:
    """
    Guarda el contenido del reporte en un archivo de texto.

    Args:
        nombre_archivo (str): Ruta del archivo donde se guardará el reporte.
        contenido (str): Contenido del reporte.
    """
    with open(nombre_archivo, mode="w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def main() -> None:
    """
    Función principal que coordina la lectura de archivos,
    la generación del reporte y su guardado en /data.
    """
    base_path = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(base_path, exist_ok=True)

    archivo_csv = os.path.join(base_path, "estudiantes.csv")
    archivo_json = os.path.join(base_path, "cursos.json")
    archivo_reporte = os.path.join(base_path, "reporte.txt")

    estudiantes = leer_csv(archivo_csv)
    cursos = leer_json(archivo_json)
    reporte = generar_reporte(estudiantes, cursos)

    console.print(Panel(reporte, title=" REPORTE FINAL", border_style="cyan"))
    guardar_reporte(archivo_reporte, reporte)
    console.print(f"\n Reporte guardado en [green]{archivo_reporte}[/green]\n")


if __name__ == "__main__":
    main()
