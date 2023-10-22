from src.calculadora.fracciones_a_numeros.fracciones_a_numeros import convertir_fraccion_a_num

def suma(num1: float, num2:float) -> float:
    sumando_num1 = convertir_fraccion_a_num(num1)
    sumando_num2 = convertir_fraccion_a_num(num2)
    return float(sumando_num1 + sumando_num2)
