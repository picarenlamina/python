# Escribe un programa que rellene una lista con 10 numeros con append. El programa debe determinar el elemento maximo de la lista
# import random

lista = []

for i in range(0,10):
    lista.append( random.randint(1,100) )

maximo = lista[0]    
for i in range(1,len(lista)):
    if maximo < lista[ i ]:
        maximo = lista[ i ]

print (f"maximo {maximo}")
