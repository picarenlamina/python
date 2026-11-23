def es_palindromo(palabra):
    limpia = palabra.lower().replace(" ", "")
    return limpia == limpia[::-1]

texto = input("Introduce una palabra o frase: ")

if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")