#Calcula el término n de la sucesión de Fibonacci."""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo1 = 0
        fibo2= 1
        for i in range(2, n + 1):
            fibo = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fibo
        return fibo
        


