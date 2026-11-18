import random
numero_secreto = random.randint(1, 10)
intentos = 3
adivinado = False
print("¡Adivina el número secreto (entre 1 y 10)!")
while not adivinado and intentos > 0:
    intentos = intentos - 1
    intento = int( input("intruduce numero " ))
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        adivinado = True  # Esto hará que el bucle termine
    elif intento < numero_secreto:
        print("El número secreto es mayor. ¡Prueba otra vez!")
    else:
        print("El número secreto es menor. ¡Prueba otra vez!")
print("Juego terminado.")
