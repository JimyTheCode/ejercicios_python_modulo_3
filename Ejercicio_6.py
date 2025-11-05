from typing import TypedDict
from rich.console import Console
from rich.table import Table

console = Console()


class Producto(TypedDict):
    """Representa un producto con nombre y precio.

    Atributos:
        nombre: Nombre del producto.
        precio: Precio del producto en pesos colombianos.
    """
    nombre: str
    precio: float


def calcular_precios_con_descuento(
    productos: list[Producto], porcentaje_descuento: float = 0.10
) -> list[float]:
    """Calcula los precios con descuento usando map() y una función lambda.

    Args:
        productos: Lista de productos con nombre y precio.
        porcentaje_descuento: Porcentaje de descuento en formato decimal (ej. 0.10 = 10 %).

    Returns:
        Lista con los precios de cada producto aplicando el descuento.

    Raises:
        ValueError: Si el porcentaje de descuento no está entre 0 y 1.
    """
    if not 0 <= porcentaje_descuento <= 1:
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 1.")

    # Uso de map y lambda según lo pedido en el ejercicio
    precios_descuento = list(
        map(
            lambda p: round(p["precio"] * (1 - porcentaje_descuento), 2),
            productos,
        )
    )
    return precios_descuento


def mostrar_tabla_precios(
    productos: list[Producto], porcentaje_descuento: float = 0.10
) -> None:
    """Muestra una tabla comparando precios originales y con descuento.

    Args:
        productos: Lista de productos con sus precios originales.
        porcentaje_descuento: Porcentaje de descuento aplicado.
    """
    precios_descuento = calcular_precios_con_descuento(productos, porcentaje_descuento)

    tabla = Table(title=f"Listado de precios con {int(porcentaje_descuento * 100)} % de descuento")
    tabla.add_column("Producto", justify="left", style="bold cyan")
    tabla.add_column("Precio Original", justify="right", style="yellow")
    tabla.add_column("Con Descuento", justify="right", style="green")

    for prod, nuevo_precio in zip(productos, precios_descuento):
        precio_original = f"$ {format(prod['precio'], ',.0f').replace(',', '.')}"
        precio_descuento = f"$ {format(nuevo_precio, ',.0f').replace(',', '.')}"
        tabla.add_row(prod["nombre"], precio_original, precio_descuento)


    console.print(tabla)


def prueba() -> None:
    """Ejecuta un ejemplo práctico en consola."""
    productos: list[Producto] = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Gorra", "precio": 25000},
    ]
    mostrar_tabla_precios(productos, 0.10)


if __name__ == "__main__":
    prueba()
