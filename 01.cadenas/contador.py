texto = input("Escribe una frase: ")

num_palabras = len(texto.split())
caracteres_sin_espacios = len(texto.replace(" ", ""))

print(f"Palabras: {num_palabras}")
print(f"Caracteres (sin espacios): {caracteres_sin_espacios}")