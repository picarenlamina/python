frase = input("Escribe una frase: ")
prohibidas = ["tonto", "estupido", "bobo"]

for censura in prohibidas:
    bloqueo = "*" * len(censura)
    frase = frase.replace(censura, bloqueo)

print(f"Resultado: {frase}")