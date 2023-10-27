"""Modulo que resuelve una expresión matemática"""
from src.calc.evaluar_expresion.evaluar_expresion import evaluar_expresion


def main():
    """ Esta función manda a llamar a la función que permite evaluar la expresión matemática """
    expresion = "(5+5)*(1.25-0.75)"
    resultado = evaluar_expresion(expresion)
    print(f"El resultado de la expresión '{expresion}' es: {resultado}")


if __name__ == "__main__":
    main()
