# Obtine siglas
nombre = input("Introduce tu nombre completo: ")
palabras = nombre.strip().split()

iniciales = ".".join([p[0].upper() for p in palabras]) + "."

print(f"Tus iniciales son: {iniciales}")