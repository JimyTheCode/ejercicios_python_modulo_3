# Ejercicio 5: Calculadora de Impuestos con Scope Global
# ------------------------------------------------------
# Conceptos aplicados: Scope Global vs. Local, uso de 'global', y Rich para visualización

from rich.console import Console
from rich.panel import Panel

console = Console()

# 🌐 Variable global
TASA_IVA = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el valor del IVA para un precio dado usando la tasa global.
    
    Args:
        precio_base (float): Precio antes de impuestos.
    
    Returns:
        float: Valor del IVA calculado.
    """
    return round(precio_base * TASA_IVA, 2)


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza la tasa global del IVA.
    
    Args:
        nueva_tasa (float): Nueva tasa de IVA (por ejemplo, 0.21 para 21%).
    """
    global TASA_IVA
    TASA_IVA = nueva_tasa
    console.print(f"[bold green]✅ Tasa de IVA actualizada a:[/bold green] {TASA_IVA * 100:.1f}%")


def mostrar_resultados(precio: float) -> None:
    """
    Muestra el resultado del cálculo del IVA con formato visual.
    """
    iva = calcular_iva(precio)
    total = precio + iva
    texto = f"""
💰 Precio base: [yellow]{precio:,.2f}[/yellow]
🧾 Tasa de IVA actual: [cyan]{TASA_IVA * 100:.1f}%[/cyan]
📊 Valor del IVA: [green]{iva:,.2f}[/green]
🏷️ Total con IVA: [bold]{total:,.2f}[/bold]
"""
    console.print(Panel(texto, title="CALCULADORA DE IVA", border_style="blue"))


if __name__ == "__main__":
    console.print(Panel("[bold cyan]💼 Ejercicio 5: Calculadora de Impuestos[/bold cyan]", border_style="cyan"))
    
    precio_base = 100000
    mostrar_resultados(precio_base)

    # Cambiamos la tasa y volvemos a calcular
    actualizar_tasa_iva(0.21)
    mostrar_resultados(precio_base)
