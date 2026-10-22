import random

lista = []

for i in range(0,10):
    lista.append( random.randint(1,100) )

maximo = 0    
for i in range(0,len(lista)):
    if maximo < lista[ i ]:
        maximo = lista[ i ]

print (f"maximo {maximo}")
