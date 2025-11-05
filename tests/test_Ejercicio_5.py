import Ejercicio_5 


def test_calcular_iva_valor_correcto():
    assert Ejercicio_5.calcular_iva(100000) == 19000.00  # 19%


def test_actualizar_tasa_iva_cambia_valor():
    Ejercicio_5.actualizar_tasa_iva(0.21)
    assert Ejercicio_5.calcular_iva(100000) == 21000.00  # 21%


def test_tasa_global_se_actualiza():
    Ejercicio_5.actualizar_tasa_iva(0.15)
    assert round(Ejercicio_5.TASA_IVA, 2) == 0.15
