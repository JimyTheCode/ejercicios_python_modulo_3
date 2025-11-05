from typing import Callable, List
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()


def aplicar_validador(datos: List, validador: Callable) -> List:
    """
    Aplica una función validadora a cada elemento de la lista y devuelve solo los válidos.

    Args:
        datos (List): Lista de elementos a validar.
        validador (Callable): Función que recibe un elemento y devuelve True si es válido.

    Returns:
        List: Nueva lista con los elementos que pasaron la validación.
    """
    if not callable(validador):
        raise TypeError("El argumento 'validador' debe ser una función.")
    return [dato for dato in datos if validador(dato)]


# ----------------------- VALIDADORES -----------------------

def es_email_valido(email: str) -> bool:
    """
    Valida si un email tiene un formato correcto básico.

    Args:
        email (str): Dirección de correo a validar.

    Returns:
        bool: True si el email es válido, False en caso contrario.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None


def es_mayor_a_10(numero: int) -> bool:
    """
    Verifica si un número es mayor a 10.

    Args:
        numero (int): Número a evaluar.

    Returns:
        bool: True si el número es mayor a 10, False en caso contrario.
    """
    return numero > 10


# ----------------------- DEMOSTRACIÓN -----------------------

def main() -> None:
    """
    Función principal: demuestra el uso de aplicar_validador con diferentes validadores.
    """
    console.print(Panel(Text("✅ VALIDADOR DE DATOS GENÉRICO", justify="center", style="bold cyan")))

    correos = ["juan@gmail.com", "maria@", "test@dominio.com", "invalid@", "correo@empresa.co"]
    numeros = [3, 11, 25, 9, 10, 18]

    correos_validos = aplicar_validador(correos, es_email_valido)
    numeros_validos = aplicar_validador(numeros, es_mayor_a_10)

    tabla = Table(title="Resultados de Validación", show_header=True, header_style="bold magenta")
    tabla.add_column("Tipo de dato")
    tabla.add_column("Entrada original", style="yellow")
    tabla.add_column("Datos válidos", style="green")

    tabla.add_row("Correos", str(correos), str(correos_validos))
    tabla.add_row("Números", str(numeros), str(numeros_validos))

    console.print(tabla)
    console.print(Panel(Text("💡 Los validadores se pueden reutilizar con cualquier tipo de dato.", justify="center", style="bold green")))


if __name__ == "__main__":
    main()