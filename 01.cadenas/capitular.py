```python
# Lee el nombre y los escribe en formato capitular
nombre_sucio = input("Introduce tu nombre y apellidos: ")

# Quita espacios al principio y al final
sin_extremos = nombre_sucio.strip()

# Separa el texto en una lista de palabras (eliminando espacios extra)
palabras = sin_extremos.split()

# Une las palabras con un solo espacio entre ellas
nombre_unido = " ".join(palabras)

# Convierte la primera letra de cada palabra a mayúscula
nombre_limpio = nombre_unido.title()

print(f"Nombre formateado: {nombre_limpio}")



