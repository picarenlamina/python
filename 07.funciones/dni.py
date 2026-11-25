def validar_dni(dni):
    letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # Limpiamos espacios y pasamos la letra a mayúscula
    dni = dni.strip().upper()
    
    #  Comprobamos que tenga exactamente 9 caracteres
    if len(dni) != 9:
        return False
        
    numero_str = dni[:8]
    letra_usuario = dni[8]
    
    #  Comprobamos que los primeros 8 sean dígitos y el último sea una letra
    if not numero_str.isdigit() or not letra_usuario.isalpha():
        return False
        
    # 3. Calculamos la letra oficial (resto de dividir el número entre 23)
    indice = int(numero_str) % 23
    letra_correcta = letras_validas[indice]
    
    return letra_usuario == letra_correcta


# --- Ejemplo de uso ---
dni_usuario = input("Introduce tu DNI (8 números y una letra): ")

if validar_dni(dni_usuario):
    print("El DNI es VÁLIDO.")
else:
    print("El DNI NO es válido.")