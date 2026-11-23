nombre_sucio = input("Introduce tu nombre y apellidos: ")

# strip() quita espacios en los extremos; split() + join() elimina espacios múltiples internos
nombre_limpio = " ".join(nombre_sucio.strip().split()).title()
print(f"Nombre formateado: {nombre_limpio}")


nombre = nombre_sucio.strip()
print(f"Nombre strip: {nombre}")
nombre = nombre.split()
print(f"Nombre split: {nombre}")
nombre = nombre.title()
print(f"Nombre formateado: {nombre}")


print(f"Nombre formateado: {nombre_limpio}")