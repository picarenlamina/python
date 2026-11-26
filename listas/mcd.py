


def mcd( a ,b):
    
    if( a > b ):
        temp = a
        a = b
        b = temp

    for i in range( a, 0, -1 ):
        if( a % i == 0 and b % i == 0 ):
            return i

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))   

print(f"El MCD de {a} y {b} es: {mcd(a,b)}")
