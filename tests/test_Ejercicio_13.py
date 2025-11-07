import json
from pathlib import Path
import pytest

from Ejercicio_13 import (
    cargar_inventario,
    agregar_producto,
    vender_producto,
    modificar_producto,
)


def escribir_inventario(path: Path, lista):
    path.write_text(json.dumps(lista, ensure_ascii=False, indent=2), encoding="utf-8")


def test_cargar_inventario_no_existe(tmp_path):
    ruta = tmp_path / "inv.json"
    assert not ruta.exists()
    inv = cargar_inventario(str(ruta))
    assert inv == []


def test_agregar_producto_y_guardar(tmp_path):
    ruta = tmp_path / "inv.json"
    inv = []
    producto = agregar_producto(inv, "Zapatos", 75000.0, 3, ruta=str(ruta))
    assert producto["id"] == 1
    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert data[0]["nombre"] == "Zapatos"
    assert data[0]["precio"] == 75000.0
    assert data[0]["stock"] == 3


def test_vender_producto_resta_stock(tmp_path):
    ruta = tmp_path / "inv.json"
    lista = [{"id": 1, "nombre": "Gorra", "precio": 25000.0, "stock": 5}]
    escribir_inventario(ruta, lista)
    inv = cargar_inventario(str(ruta))
    actualizado = vender_producto(inv, 1, 2, ruta=str(ruta))
    assert actualizado["stock"] == 3
    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert data[0]["stock"] == 3


def test_vender_producto_sin_stock_raises(tmp_path):
    ruta = tmp_path / "inv.json"
    lista = [{"id": 1, "nombre": "Correa", "precio": 15000.0, "stock": 1}]
    escribir_inventario(ruta, lista)
    inv = cargar_inventario(str(ruta))
    with pytest.raises(ValueError):
        vender_producto(inv, 1, 2, ruta=str(ruta))


def test_modificar_producto_y_guardar(tmp_path):
    ruta = tmp_path / "inv.json"
    lista = [{"id": 1, "nombre": "Pulsera", "precio": 10000.0, "stock": 4}]
    escribir_inventario(ruta, lista)
    inv = cargar_inventario(str(ruta))
    mod = modificar_producto(inv, 1, nombre="Pulsera VIP", precio=12000.0, stock=2, ruta=str(ruta))
    assert mod["nombre"] == "Pulsera VIP"
    assert mod["precio"] == 12000.0
    assert mod["stock"] == 2
    data = json.loads(ruta.read_text(encoding="utf-8"))
    assert data[0]["nombre"] == "Pulsera VIP"
