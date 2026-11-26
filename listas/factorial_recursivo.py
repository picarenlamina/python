

def factorial( n ):
    if n == 0:
        return 1
    else:
        return n * factorial( n-1 )



numero = int(input("Ingrese el número para calcular el factorial: "))

print(f"El factorial de {numero} es: {factorial(numero)}")


