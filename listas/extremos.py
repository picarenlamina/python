def maximo( lista ):
    max = lista[0]
    for i in range(len(lista)):
        if max < lista[i]:
            max = lista[i]
    return max

def minimo( lista ):
    min = lista[0]
    for i in range(len(lista)):
        if min > lista[i]:
            min = lista[i]
    return min

numero = int(input("Ingrese la cantidad de entradas: "))
numeros = []
for i in range(numero):
    numeros.append(int(input(f"Ingrese numero {i + 1}: ")))
print(f"El número máximo es: {maximo(numeros)}")
print(f"El número mínimo es: {minimo(numeros)}")
