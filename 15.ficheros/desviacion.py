
"""
Descripción: Este programa genera 100 números enteros aleatorios entre 0 y 200,
los guarda en un fichero de texto llamado 'numeros.txt', cierra el fichero,
lo vuelve a abrir para leer los datos y finalmente calcula y muestra por pantalla
la desviación estándar de los números generados.
"""

import random

# Función que calcula la media aritmética de una lista de números
def media( lista ):
    total = 0
    for i in range( 0, len( lista ) ):
        total = total + lista[ i ]
    return total / len( lista )

# Función que calcula la desviación estándar de una lista de números
def desviacion( lista ):
    total = 0
    for i in range( 0, len( lista ) ):
        total = total + pow(  lista[ i ] - media( lista ), 2  )
    return pow( total / len( lista ) , 1/2 ) 

# 1. Abrimos el fichero en modo escritura ("w") y guardamos 100 números aleatorios
f = open("numeros.txt", "w" )
for i in range( 100 ):
    numero = random.randint(0, 200)
    f.write( str( numero ) + "\n" )
f.close() # Cerramos el fichero para guardar los cambios

# 2. Abrimos el fichero en modo lectura ("r") y pasamos los datos a una lista
f = open("numeros.txt", "r" )
lista = []
for linea in f:
    lista.append( int( linea ) )
f.close() # Cerramos el fichero tras terminar de leer

# 3. Calculamos e imprimimos la desviación estándar
print( media( lista ) )
print( desviacion( lista ) )
