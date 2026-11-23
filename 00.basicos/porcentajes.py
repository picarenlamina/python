total_segundos = int(input("Introduce una cantidad de segundos: "))

horas = total_segundos // 3600 # // division entera
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{total_segundos}s son {horas}h {minutos}m {segundos}s.")