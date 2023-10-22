"""Module providing a function printing python version."""
from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


def resta(num1: float, num2: float) -> float:
    """

    Args:
      num1: float: 
      num2: float: 

    Returns:

    """
    restando_num1 = conv_fracc_num(num1)
    restando_num2 = conv_fracc_num(num2)
    return float(restando_num1 - restando_num2)
