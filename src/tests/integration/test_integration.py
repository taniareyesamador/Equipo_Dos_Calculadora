import sys

sys.path.append("src/calc")
sys.path.append("../")

import pytest

from src.calc.suma.suma import suma
from src.calc.resta.resta import resta
from src.calc.division.division import division
from src.calc.multiplicacion.multiplicacion import multiplicacion
from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


def obtener_datos_test_integracion():
    return [
        ("(5+5)*(1.25-0.75)", 5),
        ("(8+7/5)*(15-3/8)", 137.475),
    ]


@pytest.mark.parametrize("operacion, esperado", obtener_datos_test_integracion())
def test_divide_parametrize(operacion, esperado):
    assert ( == esperado)
