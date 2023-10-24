import sys

sys.path.append("src/calc")
sys.path.append("../")

import pytest

from src.calc.evaluar_expresion.evaluar_expresion import evaluar_expresion


def obtener_datos_test_integracion():
    return [
        ("(5+5)*(1.25-0.75)", 5),
        ("(8+7/5)*(15-3/8)", 137.475),
    ]


@pytest.mark.parametrize("operacion, esperado", obtener_datos_test_integracion())
def test_divide_parametrize(operacion, esperado):
    assert (evaluar_expresion(operacion) == esperado)
