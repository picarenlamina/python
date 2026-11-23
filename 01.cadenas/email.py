
password = input("Crea una contraseña: ")

tiene_longitud = len(password) >= 8
tiene_numero = False
tiene_mayuscula = False

# Recorremos la contraseña letra por letra de forma tradicional
for letra in password:
    if letra.isdigit():
        tiene_numero = True
    if letra.isupper():
        tiene_mayuscula = True

if tiene_longitud and tiene_numero and tiene_mayuscula:
    print("Contraseña válida.")
else:
    print("Contraseña débil. Debe tener al menos 8 caracteres, un número y una mayúscula.")