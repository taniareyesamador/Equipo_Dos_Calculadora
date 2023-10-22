from src.calculadora.fracciones_a_numeros.fracciones_a_numeros import convertir_fraccion_a_num

def multiplicacion(num1: float, num2:float) -> float:
    multiplicando_num1 = convertir_fraccion_a_num(num1)
    multiplicando_num2 = convertir_fraccion_a_num(num2)
    return float(multiplicando_num1 * multiplicando_num2)
