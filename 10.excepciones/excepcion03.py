def calculadora_division():
    try:
        numerador = float(input("Introduce el numerador: "))
        denominador = float(input("Introduce el denominador: "))
        resultado = numerador / denominador
    except ValueError:
        print("Error: Debes introducir valores numéricos válidos.")
    except ZeroDivisionError:
        print("Error: El denominador no puede ser cero.")
    else:
        print(f"Resultado: {resultado:.2f}")
    finally:
        print("Operación finalizada.")


# Ejemplo de uso
calculadora_division()