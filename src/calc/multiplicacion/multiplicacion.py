"""Modulo que convierte una  fracción a un número real"""
from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


def multiplicacion(num1: float, num2: float) -> float:
    """
    Esta función permite realizar la multiplicación de nos números reales

    Args:
      num1: float:
      num2: float:

    Returns: Un número real, como resultado de la multiplicación de dos números reales

    """
    multiplicando_num1 = conv_fracc_num(num1)
    multiplicando_num2 = conv_fracc_num(num2)
    return float(multiplicando_num1 * multiplicando_num2)
