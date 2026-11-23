#Programa que gnerere calificacion textual
nota = float(input("Introduce tu nota (0 - 10): "))

if nota < 0 or nota > 10:
    print("Error: La nota debe estar entre 0 y 10.")
elif nota < 5:
    print("Calificación: Insuficiente")
elif nota < 6:
    print("Calificación: Suficiente")
elif nota < 7:
    print("Calificación: Bien")
elif nota < 9:
    print("Calificación: Notable")
else:
    print("Calificación: Sobresaliente")