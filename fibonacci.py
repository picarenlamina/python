suma = 0

for i in range( 1, 101):
    suma = suma + i


fibo1 = 0
fibo2 = 1

n  = 10

if( n == 0  ):
    fibonacci = 0
elif(  n == 1 ):
    fibonacci = 1
else:
    for i in range ( 2, n + 1 ):
        fibonacci = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibonacci


print(f"El fibonacci del numero {n } es {fibonacci}")
