import sys

sys.path.append("src/calc")
sys.path.append("../")

import pytest

from src.calc.suma.suma import suma
from src.calc.resta.resta import resta
from src.calc.division.division import division
from src.calc.multiplicacion.multiplicacion import multiplicacion
from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


# Pruebas para la suma
def obtener_datos_test_suma():
    return [(1, 2, 3), ("4", "5", 9), ("10.5", 0.5, 11)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_suma())
def test_suma_parametrize(num1, num2, esperado):
    assert suma(num1, num2) == esperado


# Pruebas para la resta
def obtener_datos_test_resta():
    return [(1, 2, -1), ("9", "5", 4), ("11.5", 0.5, 11)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_resta())
def test_resta_parametrize(num1, num2, esperado):
    assert resta(num1, num2) == esperado


# Pruebas para la división
def obtener_datos_test_division():
    return [(10, 2, 5), ("9", "2", 4.5), ("20", 5, 4)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_division())
def test_division_parametrize(num1, num2, esperado):
    assert division(num1, num2) == esperado


# Pruebas para la multiplicación
def obtener_datos_test_multiplicacion():
    return [(10, 2, 20), ("9", "2", 18), ("4.5", 4.5, 20.25)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_multiplicacion())
def test_multiplicacion_parametrize(num1, num2, esperado):
    assert multiplicacion(num1, num2) == esperado


# Pruebas para la conversión de fracción a número
def obtener_datos_test_fraccion_a_num():
    return [(1/2, 0.5), ("1/4", 0.25), (4/4, 1)]


@pytest.mark.parametrize("num1, esperado", obtener_datos_test_fraccion_a_num())
def test_fraccion_a_num_parametrize(num1, esperado):
    assert conv_fracc_num(num1) == esperado
