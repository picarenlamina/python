

lista = []

for i in range(0,10):
    lista.append( i )
    
for i in range(0,len(lista)):
    print (f"lista[{i}]=>{lista[ i ] }")
lista.pop()

for i in range(0,len(lista)):
  print (f"lista[{i}]=>{lista[ i ] }")
