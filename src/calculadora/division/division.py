from src.calculadora.fracciones_a_numeros.fracciones_a_numeros import convertir_fraccion_a_num

def division(num1: float, num2:float) -> float:
    if num2 == 0:
        return print("No se puede realizar una división entre 0 (cero).")
    else:
        dividiendo_num1 = convertir_fraccion_a_num(num1)
        dividiendo_num2 = convertir_fraccion_a_num(num2)
        return float(dividiendo_num1 / dividiendo_num2)
