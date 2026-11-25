def mcd(a, b):
    if( a < b):
        temp = b
        b = a
        a = temp

    while b >=1:
        if( a % b == 0 ):
            return b
        b = b -1
    

# --- Ejemplo de uso ---
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

mcd = mcd(num1, num2)
print(f"El MCD de {num1} y {num2} es: {mcd}")