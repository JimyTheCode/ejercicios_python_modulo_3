# Ejercicio 11: Gestor de Tareas en Archivo de Texto (.txt)

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()
ARCHIVO_TAREAS = "tareas.txt"


def agregar_tarea(tarea: str) -> None:
    """Agrega una nueva tarea al archivo."""
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea.strip() + "\n")
    console.print(f"[green]  Tarea agregada:[/green] '{tarea}'")


def ver_tareas() -> list[str]:
    """Lee todas las tareas del archivo y devuelve una lista."""
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
    except FileNotFoundError:
        tareas = []
    return tareas


def mostrar_tareas(tareas: list[str]) -> None:
    """Muestra las tareas en una tabla con rich."""
    if not tareas:
        console.print(Panel("[yellow]⚠ No hay tareas registradas aún.[/yellow]", border_style="red"))
        return

    tabla = Table(title=" Lista de Tareas", header_style="bold cyan", border_style="blue")
    tabla.add_column("N°", justify="center")
    tabla.add_column("Tarea", justify="left")

    for i, tarea in enumerate(tareas, 1):
        tabla.add_row(str(i), tarea)

    console.print(tabla)


def main():
    """Función principal con menú interactivo."""
    while True:
        console.print(Panel.fit(
            "[bold cyan]=== Gestor de Tareas ===[/bold cyan]\n"
            "[1] Agregar tarea\n"
            "[2] Ver tareas\n"
            "[3] Salir",
            border_style="blue"
        ))

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
            else:
                console.print("[red] No puede ingresar una tarea vacía.[/red]")

        elif opcion == "2":
            tareas = ver_tareas()
            mostrar_tareas(tareas)

        elif opcion == "3":
            console.print(Panel("[bold red] Saliendo del gestor...[/bold red]", border_style="red"))
            break

        else:
            console.print("[yellow]⚠ Opción no válida. Intente de nuevo.[/yellow]")


if __name__ == "__main__":
    main()
