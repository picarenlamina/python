def calcular_factorial(n):
    # Validamos que sea un número entero 
    if not isinstance(n, int):
        raise TypeError("El factorial solo está definido para números enteros.")
        
    # Validamos que no sea negativo
    if n < 0:
        raise ValueError("No existe el factorial de un número negativo.")
        
    # 3. Cálculo iterativo (0! = 1 y 1! = 1)
    factorial = 1
    for i in range(2, n + 1):
        factorial  = factorial * i
        
    return factorial


# --- Programa principal con captura de excepciones ---
try:
    entrada = input("Introduce un número entero positivo para calcular su factorial: ")
    numero = int(entrada)  # Puede lanzar ValueError si el usuario escribe texto o decimales
    
    factorial = calcular_factorial(numero)
    
except ValueError as error_valor:
    print(f"Error de valor: {error_valor}")
except TypeError as error_tipo:
    print(f"Error de tipo: {error_tipo}")
else:
    print(f"El factorial de {numero} ({numero}!) es: {factorial}")