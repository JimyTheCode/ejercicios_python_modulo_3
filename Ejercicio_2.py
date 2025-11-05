from typing import Tuple, Dict
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def crear_perfil(nombre: str, edad: int, *hobbies: Tuple[str], **redes_sociales: Dict[str, str]) -> str:
    """
    Genera un perfil de usuario con nombre, edad, hobbies y redes sociales.

    Args:
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario (debe ser mayor a 0).
        *hobbies (Tuple[str]): Lista variable de hobbies.
        **redes_sociales (Dict[str, str]): Redes sociales como pares clave-valor (ej. twitter="@usuario").

    Returns:
        str: Cadena de texto formateada con la información del perfil.

    Raises:
        ValueError: Si el nombre está vacío o la edad no es válida.
    """
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if edad <= 0:
        raise ValueError("La edad debe ser mayor que 0.")

    perfil = f"👤 Nombre: {nombre}\n🎂 Edad: {edad} años\n"

    if hobbies:
        perfil += f"🎯 Hobbies: {', '.join(hobbies)}\n"
    else:
        perfil += "🎯 Hobbies: No especificados\n"

    if redes_sociales:
        redes = ", ".join([f"{k}: {v}" for k, v in redes_sociales.items()])
        perfil += f"🌐 Redes Sociales: {redes}\n"
    else:
        perfil += "🌐 Redes Sociales: No registradas\n"

    return perfil.strip()


def main() -> None:
    """
    Función principal: solicita datos al usuario y muestra el perfil formateado.
    """
    console.print(Panel(Text("👥 GENERADOR DE PERFIL DE USUARIO", justify="center", style="bold cyan")))

    # Solicitar nombre
    nombre = input("Ingrese su nombre: ").strip()
    while not nombre:
        console.print("[bold red]⚠ El nombre no puede estar vacío.[/bold red]")
        nombre = input("Ingrese su nombre: ").strip()

    # Solicitar edad
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <= 0:
                console.print("[bold red]⚠ La edad debe ser mayor que 0.[/bold red]")
                continue
            break
        except ValueError:
            console.print("[bold red]⚠ Debe ingresar un número entero válido para la edad.[/bold red]")

    # Solicitar hobbies (opcional)
    hobbies = input("Ingrese sus hobbies separados por comas (opcional): ").strip()
    lista_hobbies = tuple(h.strip() for h in hobbies.split(",") if h.strip()) if hobbies else ()

    # Solicitar redes sociales (opcional)
    redes_sociales = {}
    console.print("Ingrese sus redes sociales (ejemplo: twitter=@usuario). Deje vacío para terminar.")
    while True:
        red = input("Nombre de la red: ").strip().lower()
        if not red:
            break
        usuario = input(f"Usuario en {red}: ").strip()
        redes_sociales[red] = usuario

    perfil = crear_perfil(nombre, edad, *lista_hobbies, **redes_sociales)

    console.print(Panel(Text(perfil, style="bold green"), border_style="cyan"))


if __name__ == "__main__":
    main()
