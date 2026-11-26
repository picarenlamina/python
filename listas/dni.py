def validar_dni(dni: str) -> bool:
    # Tabla oficial de letras según el resto de dividir entre 23
    letras_validas = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    # Limpiamos espacios o guiones y pasamos a mayúsculas
    dni = dni.strip()
    dni = dni.replace("-", "")
    dni = dni.upper()
    
    # 1. Comprobar longitud exacta (9 caracteres)
    if len(dni) != 9:
        return False
        
    numero = dni[0:8]  # Los primeros 8 caracteres
    letra = dni[8]    # El último carácter
    
    # 2. Comprobar que los 8 primeros sean dígitos y el último una letra
    if not numero.isdigit() or not letra.isalpha():
        return False
        
    # 3. Calcular la letra correspondiente y comparar
    resto = int(numero) % 23
    letra_calculada = letras_validas[resto]
    
    return letra == letra_calculada


# main


dni = input("Ingrese un DNI para validar: ")

if validar_dni(dni):
    print(f"El DNI {dni} es válido.")
else:
    print(f"El DNI {dni} no es válido.")
