numero = int(input("Introduce un número entero: "))

if numero <= 1:
    print(f"{numero} no es primo.")
else:
    es_primo = True
    i = 2
    while i <  numero and not es_primo:
        if numero % i == 0:
            es_primo = False
        i += 1
            
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es primo.")