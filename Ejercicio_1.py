from rich.console import Console
from rich.panel import Panel
from rich.prompt import FloatPrompt
from rich.text import Text

console = Console()


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso en kilogramos. Debe ser mayor que 0.
        altura (float): Altura en metros. Debe ser mayor que 0.

    Returns:
        float: El valor del IMC calculado.

    Raises:
        ValueError: Si el peso o la altura no son positivos.
    """
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que 0.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que 0.")

    return peso / (altura ** 2)


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC según los rangos estándar de la OMS.

    Args:
        imc (float): Índice de Masa Corporal.

    Returns:
        str: Categoría del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc <= 50:
        return "Obesidad"
    else:
        return "Valor de IMC fuera de rango válido"


def solicitar_valor(nombre: str) -> float:
    """
    Solicita un valor numérico positivo al usuario, mostrando errores si no lo cumple.

    Args:
        nombre (str): El nombre del valor (por ejemplo 'peso' o 'altura').

    Returns:
        float: El valor ingresado válido.
    """
    while True:
        try:
            valor = FloatPrompt.ask(f"Ingrese su {nombre} en {'kg' if nombre == 'peso' else 'm'}")
            if valor <= 0:
                console.print(f"[bold red]⚠ El {nombre} debe ser mayor que 0.[/bold red]")
                continue
            return valor
        except ValueError:
            console.print(f"[bold red]⚠ Entrada inválida. Por favor ingrese un número válido para {nombre}.[/bold red]")


def main() -> None:
    """
    Función principal: pide los datos al usuario, calcula e interpreta el IMC.
    """
    console.print(Panel(Text("💪 CÁLCULO DE ÍNDICE DE MASA CORPORAL (IMC)", justify="center", style="bold cyan")))

    peso = solicitar_valor("peso")
    altura = solicitar_valor("altura")

    imc = calcular_imc(peso, altura)
    interpretacion = interpretar_imc(imc)

    color = {
        "Bajo peso": "yellow",
        "Normal": "green",
        "Sobrepeso": "magenta",
        "Obesidad": "red",
        "Valor de IMC fuera de rango válido": "grey50"
    }[interpretacion]

    resultado_texto = Text(f"Su IMC es {imc:.2f} → {interpretacion}", style=f"bold {color}")
    console.print(Panel(resultado_texto, border_style=color, expand=False))


if __name__ == "__main__":
    main()
