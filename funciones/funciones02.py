import random
import fibonacci


n_aleatorio = random.randint(1, 10)
print(f"Número aleatorio generado: {n_aleatorio}")

for i in range(n_aleatorio + 1):
    print(f"Fibonacci({i}) = {fibonacci.fibonacci(i)}")
