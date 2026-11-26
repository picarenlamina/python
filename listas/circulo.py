import math

def area( radio ):
    return 3.14 * math.pow( radio , 2 )    
 

def longitud( radio ):
    return 2 * 3.14 * radio



radio = int(input("Ingrese el radio del círculo: "))

print(f"El área del círculo es: {area(radio)}")
print(f"La longitud del círculo es: {longitud(radio)}") 

