"""
Ejercicio 15: Mini Sistema de Biblioteca (mejorado)

"""

import json
from pathlib import Path
from typing import List, Optional, TypedDict

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
BIBLIOTECA_FILE = "biblioteca.json"


class Libro(TypedDict):
    """Tipo que representa un libro en la biblioteca."""
    libro_id: str
    titulo: str
    autor: Optional[str]
    prestado_a: Optional[str]


def cargar_biblioteca(ruta: str = BIBLIOTECA_FILE) -> List[Libro]:
    """
    Carga la lista de libros desde un archivo JSON.

    Si el archivo no existe, devuelve una lista vacía.

    Args:
        ruta: Ruta al archivo JSON.

    Returns:
        Lista de libros.
    """
    path = Path(ruta)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as fh:
            datos = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON inválido en {ruta}: {exc}") from exc
    if not isinstance(datos, list):
        raise ValueError("El archivo debe contener una lista de libros.")
    libros: List[Libro] = []
    for item in datos:
        libros.append({
            "libro_id": str(item.get("libro_id")),
            "titulo": str(item.get("titulo", "")),
            "autor": item.get("autor"),
            "prestado_a": item.get("prestado_a"),
        })
    return libros


def guardar_biblioteca(libros: List[Libro], ruta: str = BIBLIOTECA_FILE) -> None:
    """
    Guarda la lista de libros en el archivo JSON.

    Args:
        libros: Lista de libros a guardar.
        ruta: Ruta al archivo JSON.
    """
    path = Path(ruta)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(libros, fh, ensure_ascii=False, indent=2)


def generar_nuevo_id(libros: List[Libro]) -> str:
    """
    Genera un nuevo id incremental con padding (ej. "001", "002", ...).

    Args:
        libros: Lista actual de libros.

    Returns:
        Nuevo id como cadena.
    """
    max_id = 0
    for lb in libros:
        try:
            val = int(lb["libro_id"])
            if val > max_id:
                max_id = val
        except Exception:
            continue
    nuevo = max_id + 1
    return f"{nuevo:03d}"


def agregar_libro(libros: List[Libro], titulo: str, autor: Optional[str] = None,
                  ruta: str = BIBLIOTECA_FILE, libro_id: Optional[str] = None) -> Libro:
    """
    Agrega un libro al inventario y guarda el archivo.

    Args:
        libros: Lista actual de libros.
        titulo: Título del libro.
        autor: Autor (opcional).
        ruta: Ruta del archivo JSON donde se guarda el estado.
        libro_id: Id a utilizar (opcional). Si no se pasa, se genera uno nuevo.

    Returns:
        El libro agregado.
    """
    if libro_id is None:
        libro_id = generar_nuevo_id(libros)
    nuevo: Libro = {"libro_id": str(libro_id), "titulo": titulo, "autor": autor, "prestado_a": None}
    libros.append(nuevo)
    guardar_biblioteca(libros, ruta)
    return nuevo


def eliminar_libro(libros: List[Libro], libro_id: str, ruta: str = BIBLIOTECA_FILE) -> Libro:
    """
    Elimina un libro del inventario y guarda el archivo.

    Args:
        libros: Lista actual de libros.
        libro_id: Id del libro a eliminar.
        ruta: Ruta del archivo JSON donde se guarda el estado.

    Returns:
        El libro eliminado.

    Raises:
        ValueError: Si no se encuentra el libro.
    """
    for i, lb in enumerate(libros):
        if lb["libro_id"] == libro_id:
            eliminado = libros.pop(i)
            guardar_biblioteca(libros, ruta)
            return eliminado
    raise ValueError("Libro no encontrado.")


def buscar_indice_por_id(libros: List[Libro], libro_id: str) -> Optional[int]:
    """
    Devuelve el índice del libro con el id dado o None si no existe.

    Args:
        libros: Lista de libros.
        libro_id: Identificador a buscar.

    Returns:
        Índice del libro o None.
    """
    for i, lb in enumerate(libros):
        if lb["libro_id"] == libro_id:
            return i
    return None


def prestar_libro(libros: List[Libro], libro_id: str, nombre_aprendiz: str,
                  ruta: str = BIBLIOTECA_FILE) -> Libro:
    """
    Marca un libro como prestado a un aprendiz y guarda el estado.

    Args:
        libros: Lista actual de libros.
        libro_id: Id del libro a prestar.
        nombre_aprendiz: Nombre de quien toma el libro.
        ruta: Ruta al archivo JSON donde se guardará el estado.

    Returns:
        El libro actualizado.

    Raises:
        ValueError: Si el libro no existe o ya está prestado.
    """
    idx = buscar_indice_por_id(libros, libro_id)
    if idx is None:
        raise ValueError("Libro no encontrado.")
    if libros[idx]["prestado_a"]:
        raise ValueError("El libro ya está prestado.")
    libros[idx]["prestado_a"] = nombre_aprendiz
    guardar_biblioteca(libros, ruta)
    return libros[idx]


def devolver_libro(libros: List[Libro], libro_id: str,
                   ruta: str = BIBLIOTECA_FILE) -> Libro:
    """
    Marca un libro como devuelto (prestado_a = None) y guarda el estado.

    Args:
        libros: Lista actual de libros.
        libro_id: Id del libro a devolver.
        ruta: Ruta al archivo JSON donde se guardará el estado.

    Returns:
        El libro actualizado.

    Raises:
        ValueError: Si el libro no existe o no está prestado.
    """
    idx = buscar_indice_por_id(libros, libro_id)
    if idx is None:
        raise ValueError("Libro no encontrado.")
    if not libros[idx]["prestado_a"]:
        raise ValueError("El libro no está prestado.")
    libros[idx]["prestado_a"] = None
    guardar_biblioteca(libros, ruta)
    return libros[idx]


def buscar_libro(libros: List[Libro], query: str) -> List[Libro]:
    """
    Busca libros por título (búsqueda parcial, insensible a mayúsculas).

    Args:
        libros: Lista de libros.
        query: Texto de búsqueda.

    Returns:
        Lista de libros que coinciden.
    """
    q = query.strip().lower()
    if not q:
        return []
    return [lb for lb in libros if q in lb["titulo"].lower()]


def ver_libros_prestados(libros: List[Libro]) -> List[Libro]:
    """
    Devuelve la lista de libros que actualmente están prestados.

    Args:
        libros: Lista de libros.

    Returns:
        Lista de libros prestados.
    """
    return [lb for lb in libros if lb["prestado_a"]]


def crear_tabla_libros(libros: List[Libro]) -> Table:
    """
    Crea una tabla rich a partir de una lista de libros (no imprime).

    Args:
        libros: Lista de libros.

    Returns:
        rich.table.Table con la representación.
    """
    tabla = Table(title="📚 Biblioteca", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Título", style="bold")
    tabla.add_column("Autor")
    tabla.add_column("Prestado a", justify="center")
    for lb in libros:
        tabla.add_row(
            lb["libro_id"],
            lb["titulo"],
            str(lb.get("autor") or "-"),
            str(lb.get("prestado_a") or "-"),
        )
    return tabla


def mostrar_libros(libros: List[Libro]) -> None:
    """
    Muestra en consola todos los libros usando rich.

    Args:
        libros: Lista de libros.
    """
    if not libros:
        console.print(Panel("[yellow]No hay libros en la biblioteca.[/yellow]"))
        return
    tabla = crear_tabla_libros(libros)
    console.print(tabla)


def mostrar_libros_prestados(libros: List[Libro]) -> None:
    """
    Muestra en consola los libros prestados usando rich.

    Args:
        libros: Lista de libros.
    """
    prestados = ver_libros_prestados(libros)
    if not prestados:
        console.print(Panel("[green]No hay libros prestados.[/green]"))
        return
    tabla = crear_tabla_libros(prestados)
    console.print(Panel("[bold]Libros prestados[/bold]", style="blue"))
    console.print(tabla)


def mostrar_busqueda(libros: List[Libro], query: str) -> None:
    """
    Busca y muestra en consola los libros que coinciden con la query.

    Args:
        libros: Lista de libros.
        query: Texto de búsqueda.
    """
    resultados = buscar_libro(libros, query)
    if not resultados:
        console.print(Panel(f"[yellow]No se encontraron libros para: {query}[/yellow]"))
        return
    tabla = crear_tabla_libros(resultados)
    console.print(Panel(f"[bold]Resultados para: {query}[/bold]", style="green"))
    console.print(tabla)


def mostrar_menu() -> None:
    """Muestra el menú interactivo en consola."""
    console.print(Panel.fit(
        "[bold cyan]=== Mini Biblioteca ===[/bold cyan]\n"
        "[1] Ver todos los libros\n"
        "[2] Agregar libro\n"
        "[3] Eliminar libro\n"
        "[4] Buscar libro por título\n"
        "[5] Ver libros prestados\n"
        "[6] Prestar libro\n"
        "[7] Devolver libro\n"
        "[8] Salir",
        border_style="bright_blue"
    ))


def main() -> None:
    """Bucle principal del programa con menú interactivo y persistencia."""
    ruta = str(Path.cwd() / BIBLIOTECA_FILE)
    try:
        libros = cargar_biblioteca(ruta)
    except ValueError as exc:
        console.print(f"[red]Error al cargar la biblioteca:[/red] {exc}")
        libros = []

    while True:
        mostrar_menu()
        opcion = Prompt.ask("Seleccione una opción", choices=[str(i) for i in range(1, 9)])
        if opcion == "1":
            mostrar_libros(libros)
        elif opcion == "2":
            titulo = Prompt.ask("Título del libro").strip()
            autor = Prompt.ask("Autor (opcional)", default="").strip() or None
            nuevo = agregar_libro(libros, titulo, autor, ruta=ruta)
            console.print(f"[green]✅ Libro agregado (ID: {nuevo['libro_id']})[/green]")
        elif opcion == "3":
            lid = Prompt.ask("ID del libro a eliminar").strip()
            try:
                eliminado = eliminar_libro(libros, lid, ruta=ruta)
                console.print(f"[green]✅ Libro eliminado: {eliminado['titulo']}[/green]")
            except ValueError as exc:
                console.print(f"[red]❌ {exc}[/red]")
        elif opcion == "4":
            q = Prompt.ask("Texto a buscar en título").strip()
            mostrar_busqueda(libros, q)
        elif opcion == "5":
            mostrar_libros_prestados(libros)
        elif opcion == "6":
            lid = Prompt.ask("ID del libro a prestar").strip()
            aprendiz = Prompt.ask("Nombre del aprendiz").strip()
            try:
                prestar_libro(libros, lid, aprendiz, ruta=ruta)
                console.print(f"[green]✅ Libro {lid} prestado a {aprendiz}[/green]")
            except ValueError as exc:
                console.print(f"[red]❌ {exc}[/red]")
        elif opcion == "7":
            lid = Prompt.ask("ID del libro a devolver").strip()
            try:
                devolver_libro(libros, lid, ruta=ruta)
                console.print(f"[green]✅ Libro {lid} devuelto[/green]")
            except ValueError as exc:
                console.print(f"[red]❌ {exc}[/red]")
        elif opcion == "8":
            console.print(Panel("[bold red]👋 Saliendo...[/bold red]"))
            break


if __name__ == "__main__":
    main()
