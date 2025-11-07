import csv
from typing import Dict, List
from rich.console import Console
from rich.table import Table


def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """
    Analiza una columna numérica de un archivo CSV y calcula promedio, máximo y mínimo.

    Args:
        nombre_archivo (str): Ruta al archivo CSV.
        columna (str): Nombre de la columna numérica a analizar.

    Returns:
        Dict[str, float]: Diccionario con las claves "promedio", "maximo" y "minimo",
                          cuyos valores son floats redondeados a 2 decimales.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si la columna no existe o no se encuentran valores numéricos.
        csv.Error: Si ocurre un error al leer el CSV.
    """
    valores: List[float] = []

    with open(nombre_archivo, newline="", encoding="utf-8") as fh:
        lector = csv.DictReader(fh)
        if lector.fieldnames is None:
            raise ValueError("El archivo CSV no tiene encabezados.")
        if columna not in lector.fieldnames:
            raise ValueError(f"La columna '{columna}' no se encuentra en el CSV.")

        for fila in lector:
            raw = fila.get(columna, "")
            if raw is None:
                continue
            raw_str = raw.strip()
            if raw_str == "":
                continue
            try:
                numero = float(raw_str)
            except ValueError:
                continue
            valores.append(numero)

    if not valores:
        raise ValueError(f"No se encontraron valores numéricos en la columna '{columna}'.")

    promedio = round(sum(valores) / len(valores), 2)
    maximo = round(max(valores), 2)
    minimo = round(min(valores), 2)

    return {"promedio": promedio, "maximo": maximo, "minimo": minimo}


def mostrar_resultado_analisis(
    resultado: Dict[str, float], nombre_archivo: str, columna: str
) -> None:
    """
    Muestra en consola una tabla con el resultado del análisis (promedio, max, min).

    Args:
        resultado (Dict[str, float]): Diccionario resultado de `analizar_csv`.
        nombre_archivo (str): Nombre del archivo analizado (solo para mostrar contexto).
        columna (str): Nombre de la columna analizada.
    """
    console = Console()
    tabla = Table(title=f"Análisis - {nombre_archivo} - columna: {columna}", show_lines=True)
    tabla.add_column("Métrica", style="cyan", justify="left")
    tabla.add_column("Valor", style="green", justify="right")

    tabla.add_row("Promedio", f"{resultado['promedio']:.2f}")
    tabla.add_row("Máximo", f"{resultado['maximo']:.2f}")
    tabla.add_row("Mínimo", f"{resultado['minimo']:.2f}")

    console.print(tabla)


if __name__ == "__main__":
    ejemplo = "estudiantes_demo.csv"
    try:
        with open(ejemplo, "x", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["nombre", "edad", "calificacion"])
            writer.writerow(["Ana", "20", "4.5"])
            writer.writerow(["Juan", "22", "3.2"])
            writer.writerow(["María", "19", "4.8"])
            writer.writerow(["Luis", "21", "notas"])  
    except FileExistsError:
        pass

    try:
        resultado_demo = analizar_csv(ejemplo, "calificacion")
        mostrar_resultado_analisis(resultado_demo, ejemplo, "calificacion")
    except Exception as exc:  
        Console().print(f"[red]Error:[/red] {exc}")
