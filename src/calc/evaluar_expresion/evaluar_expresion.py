"""Importación de módulos"""
from src.calc.suma.suma import suma
from src.calc.resta.resta import resta
from src.calc.division.division import division
from src.calc.multiplicacion.multiplicacion import multiplicacion


def evaluar_expresion(expresion: str) -> float:
    """
    Esta función permite realizar la evaluación de una expresión matemática que cuente con paréntesis

    Args:
      expresion: str:

    Returns: Un número real

    """

    # Elimina espacios en blanco de la expresión
    expresion = expresion.replace(" ", "")

    # Inicializa pilas para operandos y operadores
    operandos = []
    operadores = []

    i = 0
    while i < len(expresion):
        if expresion[i].isdigit() or (i < len(expresion) - 1 and expresion[i] == "-" and (i == 0 or expresion[i - 1] in "+-*/(")):
            j = i
            while j < len(expresion) and (expresion[j].isdigit() or expresion[j] == "."):
                j += 1
            operandos.append(float(expresion[i:j]))
            i = j
        elif expresion[i] in "+-*/":
            while (
                operadores
                and operadores[-1] in "+-*/"
                and (
                    (expresion[i] in "+-" and expresion[i] in "+-")
                    or (expresion[i] in "*/" and operadores[-1] in "*/")
                )
            ):
                operador = operadores.pop()
                operand2 = operandos.pop()
                operand1 = operandos.pop()
                if operador == "+":
                    result = suma(operand1, operand2)
                elif operador == "-":
                    result = resta(operand1, operand2)
                elif operador == "*":
                    result = multiplicacion(operand1, operand2)
                elif operador == "/":
                    result = division(operand1, operand2)
                operandos.append(result)
            operadores.append(expresion[i])
            i += 1
        elif expresion[i] == "(":
            # Si el carácter actual es un paréntesis de apertura,
            # simplemente agréguelo a la pila de operadores.
            operadores.append(expresion[i])
            i += 1
        elif expresion[i] == ")":
            # Si el carácter actual es un paréntesis de cierre,
            # realiza cálculos hasta encontrar el paréntesis de apertura correspondiente.
            while operadores and operadores[-1] != "(":
                operador = operadores.pop()
                operand2 = operandos.pop()
                operand1 = operandos.pop()
                if operador == "+":
                    result = suma(operand1, operand2)
                elif operador == "-":
                    result = resta(operand1, operand2)
                elif operador == "*":
                    result = multiplicacion(operand1, operand2)
                elif operador == "/":
                    result = division(operand1, operand2)
                operandos.append(result)
            if operadores and operadores[-1] == "(":
                operadores.pop()
            else:
                raise ValueError("Paréntesis desbalanceados")
            i += 1
        else:
            raise ValueError("Carácter no válido en la expresión")

    # Realiza cálculos finales si quedan operadores en la pila
    while operadores:
        operador = operadores.pop()
        operand2 = operandos.pop()
        operand1 = operandos.pop()
        if operador == "+":
            result = suma(operand1, operand2)
        elif operador == "-":
            result = resta(operand1, operand2)
        elif operador == "*":
            result = multiplicacion(operand1, operand2)
        elif operador == "/":
            result = division(operand1, operand2)
        operandos.append(result)

    # El resultado final debe estar en la cima de la pila de operandos
    if len(operandos) == 1:
        return operandos[0]
    raise ValueError("Expresión inválida")
