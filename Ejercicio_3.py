from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def crear_contador():
    """
    Crea un contador independiente que mantiene su propio estado interno.

    Returns:
        function: Una función interna que incrementa y devuelve el valor del conteo.

    Ejemplo:
        >>> contador1 = crear_contador()
        >>> contador1()
        1
        >>> contador1()
        2
        >>> contador2 = crear_contador()
        >>> contador2()
        1
    """
    conteo = 0

    def incrementar() -> int:
        """
        Incrementa el valor del contador y lo devuelve.

        Returns:
            int: El valor actual del conteo después de incrementarlo.
        """
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def main() -> None:
    """
    Función principal: demuestra el funcionamiento de varios contadores independientes.
    """
    console.print(Panel(Text("🔢 CONTADOR DE LLAMADAS CON CLOSURE", justify="center", style="bold cyan")))

    contador_a = crear_contador()
    contador_b = crear_contador()

    console.print("[bold yellow]→ Probando contador A:[/bold yellow]")
    for _ in range(3):
        console.print(f"Contador A: {contador_a()}")

    console.print("\n[bold green]→ Probando contador B (independiente):[/bold green]")
    for _ in range(2):
        console.print(f"Contador B: {contador_b()}")

    console.print("\n[bold cyan]✅ Cada contador mantiene su propio estado independiente.[/bold cyan]")


if __name__ == "__main__":
    main()
