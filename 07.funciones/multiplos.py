def multiplos(a, b):
    if( a < b):
        temp = b
        b = a
        a = temp
    if b == 0:
        return False
    if a % b == 0:
        return True
    else:
        return False 


# Ejemplos de uso
   
print(f"los numeros 3 y14 { multiplos(3, 14)}")   
print(f"los numeros 20 y 5 {multiplos(20, 5)}")
print(f"los numeros 10 y 0 {multiplos(10, 0)}")   
