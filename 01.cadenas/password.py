password = input("Introduce una contraseña: ")

especiales = "?¿@#$%&"
tiene_especial = False
tiene_mayuscula = False

for i in range(len(password)):
    letra = password[i]
    
    if especiales.find(letra) != -1:
        tiene_especial = True
        
    if letra.isupper():
        tiene_mayuscula = True

if len(password) >= 8 and tiene_especial and tiene_mayuscula:
    print("Contraseña válida.")
else:
    print("Contraseña inválida. Debe tener al menos 8 caracteres, una mayúscula y un carácter especial (?¿@#$%&).")
