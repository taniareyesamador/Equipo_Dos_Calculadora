"""Module providing a function printing python version."""
from src.calc.evaluar_expresion.evaluar_expresion import evaluar_expresion


def main():
    """ Prueba """
    expresion = "(5+5)*(1.25-0.75)"
    resultado = evaluar_expresion(expresion)
    print(f"El resultado de la expresión '{expresion}' es: {resultado}")


if __name__ == "__main__":
    main()
