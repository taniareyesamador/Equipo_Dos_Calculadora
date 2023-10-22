from src.calc.suma.suma import suma
from src.calc.resta.resta import resta
from src.calc.division.division import division
from src.calc.multiplicacion.multiplicacion import multiplicacion


def main():
    resp_division = division(10, "2")
    print(f"Resultado Division: {resp_division}")

    resp_multiplicacion = multiplicacion(10, 2)
    print(f"Resultado Multiplicacion: {resp_multiplicacion}")

    resp_suma = suma(10, 2)
    print(f"Resultado Suma: {resp_suma}")

    resp_resta = resta(10, 2)
    print(f"Resultado Resta: {resp_resta}")


if __name__ == "__main__":
    main()
