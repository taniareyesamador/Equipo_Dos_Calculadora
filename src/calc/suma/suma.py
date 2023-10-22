from src.calc.fracciones_a_numeros.fracciones_a_numeros import conv_fracc_num


def suma(num1: float, num2: float) -> float:
    sumando_num1 = conv_fracc_num(num1)
    sumando_num2 = conv_fracc_num(num2)
    return float(sumando_num1 + sumando_num2)
