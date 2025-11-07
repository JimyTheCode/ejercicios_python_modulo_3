import json
from typing import List, TypedDict, Optional
from pathlib import Path
from rich.console import Console
from rich.table import Table

Console = Console()
INVENTARIO_FILE = "inventario.json"


class Producto(TypedDict):
    """Tipo para representar un producto en inventario."""
    id: int
    nombre: str
    precio: float
    stock: int


def cargar_inventario(ruta: str = INVENTARIO_FILE) -> List[Producto]:
    """
    Carga el inventario desde un archivo JSON.

    Si el archivo no existe, retorna una lista vacía.

    Args:
        ruta: Ruta al archivo JSON.

    Returns:
        Lista de productos (posiblemente vacía).

    Raises:
        ValueError: Si el archivo existe pero no contiene JSON válido.
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
        raise ValueError("El inventario debe ser una lista de productos.")
    return [cast_producto(p) for p in datos]


def guardar_inventario(inventario: List[Producto], ruta: str = INVENTARIO_FILE) -> None:
    """
    Guarda la lista de productos en el archivo JSON.

    Args:
        inventario: Lista de productos a guardar.
        ruta: Ruta al archivo JSON.
    """
    path = Path(ruta)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(inventario, fh, ensure_ascii=False, indent=2)


def generar_nuevo_id(inventario: List[Producto]) -> int:
    """
    Genera un nuevo id único incremental para un producto.

    Args:
        inventario: Lista actual de productos.

    Returns:
        Un entero con el nuevo id (1 si está vacío).
    """
    if not inventario:
        return 1
    max_id = max(p["id"] for p in inventario)
    return max_id + 1


def cast_producto(d: dict) -> Producto:
    """
    Normaliza dict a Producto asegurando tipos correctos.

    Args:
        d: Diccionario con claves id, nombre, precio, stock.

    Returns:
        Producto con tipos convertidos.
    """
    return {
        "id": int(d.get("id")),
        "nombre": str(d.get("nombre")),
        "precio": float(d.get("precio")),
        "stock": int(d.get("stock")),
    }


def agregar_producto(
    inventario: List[Producto],
    nombre: str,
    precio: float,
    stock: int = 1,
    ruta: str = INVENTARIO_FILE,
) -> Producto:
    """
    Agrega un producto al inventario, lo guarda en el archivo y devuelve el producto creado.

    Args:
        inventario: Lista actual de productos.
        nombre: Nombre del nuevo producto.
        precio: Precio unitario (float).
        stock: Cantidad inicial (int).
        ruta: Ruta del archivo JSON donde se guardará el inventario.

    Returns:
        El producto agregado (con id asignado).
    """
    nuevo_id = generar_nuevo_id(inventario)
    producto: Producto = {"id": nuevo_id, "nombre": nombre, "precio": float(precio), "stock": int(stock)}
    inventario.append(producto)
    guardar_inventario(inventario, ruta)
    return producto


def vender_producto(
    inventario: List[Producto],
    producto_id: int,
    cantidad: int = 1,
    ruta: str = INVENTARIO_FILE,
) -> Producto:
    """
    Registra la venta de una cantidad de un producto (reduce stock) y guarda el inventario.

    Args:
        inventario: Lista actual de productos.
        producto_id: Id del producto a vender.
        cantidad: Cantidad a vender.
        ruta: Ruta del archivo JSON donde se guardará el inventario.

    Returns:
        Producto actualizado.

    Raises:
        ValueError: Si no existe el producto o no hay stock suficiente.
    """
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que 0.")

    for prod in inventario:
        if prod["id"] == producto_id:
            if prod["stock"] < cantidad:
                raise ValueError("Stock insuficiente para realizar la venta.")
            prod["stock"] -= cantidad
            guardar_inventario(inventario, ruta)
            return prod
    raise ValueError("Producto no encontrado.")


def modificar_producto(
    inventario: List[Producto],
    producto_id: int,
    nombre: Optional[str] = None,
    precio: Optional[float] = None,
    stock: Optional[int] = None,
    ruta: str = INVENTARIO_FILE,
) -> Producto:
    """
    Modifica datos de un producto y guarda el inventario.

    Args:
        inventario: Lista actual de productos.
        producto_id: Id del producto a modificar.
        nombre: Nuevo nombre (opcional).
        precio: Nuevo precio (opcional).
        stock: Nuevo stock (opcional).
        ruta: Ruta del archivo JSON donde se guardará el inventario.

    Returns:
        Producto modificado.

    Raises:
        ValueError: Si no se encuentra el producto.
    """
    for prod in inventario:
        if prod["id"] == producto_id:
            if nombre is not None:
                prod["nombre"] = nombre
            if precio is not None:
                prod["precio"] = float(precio)
            if stock is not None:
                prod["stock"] = int(stock)
            guardar_inventario(inventario, ruta)
            return prod
    raise ValueError("Producto no encontrado.")


def mostrar_inventario(inventario: List[Producto]) -> Table:
    """
    Crea y retorna una tabla rich con el inventario (no imprime directamente).

    Args:
        inventario: Lista de productos.

    Returns:
        rich.table.Table con la representación del inventario.
    """
    tabla = Table(title="📦 Inventario", show_lines=True)
    tabla.add_column("ID", justify="right", style="cyan")
    tabla.add_column("Nombre", style="bold")
    tabla.add_column("Precio", justify="right")
    tabla.add_column("Stock", justify="right")

    for prod in inventario:
        precio_str = f"$ {format(prod['precio'], ',.0f').replace(',', '.')}"
        tabla.add_row(str(prod["id"]), prod["nombre"], precio_str, str(prod["stock"]))

    return tabla


if __name__ == "__main__":
    inv = cargar_inventario()
    if not inv:
        inv = []
        agregar_producto(inv, "Camisa", 50000.0, 10)
        agregar_producto(inv, "Pantalón", 80000.0, 5)
    tabla = mostrar_inventario(inv)
    Console.print(tabla)
