# • Almacenar datos: Crea una lista con los días de la semana ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes"). Pide al usuario por teclado cuánto dinero ha gastado cada día y guárdalo en una segunda lista llamada gastos (recuerda convertir la entrada a número decimal usando float()).
# • Resumen diario: Muestra por pantalla un resumen con el formato: "El [día] gastaste [cantidad] euros."
# • Total y media: Calcula y muestra el gasto total de la semana y el gasto medio diario.
# • Días de mayor y menor gasto: Encuentra cuál fue el gasto máximo y el gasto mínimo de la semana, e imprime qué día (o días, si hay empate) corresponden a esas cantidades.
# • Reto extra (Filtro): Pide al usuario que introduzca un límite de presupuesto diario y muestra qué días superó ese límite.subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
gastos = []

#  Almacenar datos 
for dia in dias:
    gasto = float(input("¿Cuánto gastaste el " + dia + "? "))
    gastos.append(gasto)


#  Calcular total y media
suma = 0
for i in range(len(dias)):
    suma += gastos[i]

media = suma / len(dias)
print("\nEl gasto total de la semana es:", suma, "euros.")
print(f"El gasto medio diario es: {media} euros")

# 4. Calcular días con gasto máximo y mínimo
gasto_maximo = gastos[0]
gasto_minimo = gastos[0]

for i in range(len(dias)):
    if gastos[i] > gasto_maximo:
        gasto_maximo = gastos[i]
    if gastos[i] < gasto_minimo:
        gasto_minimo = gastos[i]

print("\n--- Maximo y Minimo ---")
for i in range(len(dias)):
    if gastos[i] == gasto_maximo:
        print("El día de mayor gasto fue el", dias[i], "con", gastos[i], "euros.")
    if gastos[i] == gasto_minimo:
        print("El día de menor gasto fue el", dias[i], "con", gastos[i], "euros.")

# 5. Reto extra: filtrar por presupuesto
limite = float(input("\nIntroduce tu límite de presupuesto diario: "))
print("Días en los que superaste el límite:")

for i in range(len(dias)):
    if gastos[i] > limite:
        print("-", dias[i], "(", gastos[i], "euros )")