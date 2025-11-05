import pytest
from Ejercicio_1 import calcular_imc, interpretar_imc


# ------------------ TESTS CALCULAR_IMC ------------------

def test_calcular_imc_valores_validos():
    """Debe calcular correctamente el IMC para valores válidos."""
    imc = calcular_imc(70, 1.75)
    assert round(imc, 2) == 22.86  # valor esperado exacto

def test_calcular_imc_peso_invalido():
    """Debe lanzar ValueError si el peso es 0 o negativo."""
    with pytest.raises(ValueError, match="peso debe ser mayor que 0"):
        calcular_imc(0, 1.75)
    with pytest.raises(ValueError, match="peso debe ser mayor que 0"):
        calcular_imc(-5, 1.75)

def test_calcular_imc_altura_invalida():
    """Debe lanzar ValueError si la altura es 0 o negativa."""
    with pytest.raises(ValueError, match="altura debe ser mayor que 0"):
        calcular_imc(70, 0)
    with pytest.raises(ValueError, match="altura debe ser mayor que 0"):
        calcular_imc(70, -1.75)

# ------------------ TESTS INTERPRETAR_IMC ------------------

@pytest.mark.parametrize("imc,resultado", [
    (17.0, "Bajo peso"),
    (22.0, "Normal"),
    (27.0, "Sobrepeso"),
    (33.0, "Obesidad"),
    (60.0, "Valor de IMC fuera de rango válido")
])
def test_interpretar_imc(imc, resultado):
    """Debe devolver la interpretación correcta según el rango."""
    assert interpretar_imc(imc) == resultado
