"""Module providing a function printing python version."""
from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


def division(num1: float, num2: float) -> float:
    """

    Args:
      num1: float:
      num2: float:

    Returns:

    """
    if float(num2) == 0:
        return "No se puede realizar una división entre 0 (cero)."

    dividiendo_num1 = conv_fracc_num(num1)
    dividiendo_num2 = conv_fracc_num(num2)
    return float(dividiendo_num1 / dividiendo_num2)
