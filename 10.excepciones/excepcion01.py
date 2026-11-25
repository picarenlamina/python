def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None


# Ejemplos de uso
print(dividir_seguro(10, 2))  # Salida: 5.0
print(dividir_seguro(10, 0))  # Salida: Error... -> None