def media( max, min ):
    return (max + min) / 2

dias = int(input("Ingrese la cantidad de días: "))

total = 0
for dia in range(dias):
    max = float(input(f"Ingrese la temperatura máxima del día {dia + 1}: "))
    min = float(input(f"Ingrese la temperatura mínima del día {dia + 1}: "))
    total += media(max, min)
    print(f"La temperatura media del día {dia + 1} es: {media(max, min)}")

print(f"La temperatura media del periodo es: {total / dias}")
