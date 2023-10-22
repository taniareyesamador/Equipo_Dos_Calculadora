from src.calculadora.fracciones_a_numeros.fracciones_a_numeros import convertir_fraccion_a_num

def resta(num1: float, num2:float) -> float:
    restando_num1 = convertir_fraccion_a_num(num1)
    restando_num2 = convertir_fraccion_a_num(num2)
    return float(restando_num1 - restando_num2)
