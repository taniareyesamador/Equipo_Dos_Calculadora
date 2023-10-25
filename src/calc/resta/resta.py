"""Modulo que convierte una  fracción a un número real"""
from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


def resta(num1: float, num2: float) -> float:
    """
    Esta función permite realizar la resta de nos números reales

    Args:
      num1: float:
      num2: float:

    Returns:

    Returns: Un número real, como resultado de la resta de dos números reales

    """
    restando_num1 = conv_fracc_num(num1)
    restando_num2 = conv_fracc_num(num2)
    return float(restando_num1 - restando_num2)
