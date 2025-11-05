import pytest
from Ejercicio_6 import calcular_precios_con_descuento, Producto


def test_descuento_basico():
    productos: list[Producto] = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
    ]
    resultado = calcular_precios_con_descuento(productos, 0.10)
    assert resultado == [45000.00, 72000.00]


def test_descuento_cero_por_ciento():
    productos: list[Producto] = [{"nombre": "Zapatos", "precio": 100000}]
    resultado = calcular_precios_con_descuento(productos, 0.0)
    assert resultado == [100000.00]


def test_descuento_cien_por_ciento():
    productos: list[Producto] = [{"nombre": "Sombrero", "precio": 20000}]
    resultado = calcular_precios_con_descuento(productos, 1.0)
    assert resultado == [0.00]


def test_lista_vacia():
    productos: list[Producto] = []
    resultado = calcular_precios_con_descuento(productos, 0.10)
    assert resultado == []


def test_valores_invalidos():
    productos: list[Producto] = [{"nombre": "Bolso", "precio": 50000}]
    with pytest.raises(ValueError):
        calcular_precios_con_descuento(productos, -0.1)
    with pytest.raises(ValueError):
        calcular_precios_con_descuento(productos, 1.5)
