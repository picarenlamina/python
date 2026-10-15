import random

# Generamos un número entero aleatorio entre 1 y 10 (ambos incluidos)
numero_secreto = random.randint(1, 10)
adivinado = False

print("¡Adivina el número secreto (entre 1 y 10)!")

while not adivinado:
    # Pedimos el número y lo convertimos a entero
    intento = int(input("Introduce tu número: "))
    
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        adivinado = True  # Esto hará que el bucle termine
    elif intento < numero_secreto:
        print("El número secreto es mayor. ¡Prueba otra vez!")
    else:
        print("El número secreto es menor. ¡Prueba otra vez!")

print("Juego terminado.")
