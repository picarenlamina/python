def es_correo_valido(correo):
    correo = correo.strip()

    # No debe tener espacios (find != -1 significa que encontró un espacio)
    # Ni más/menos de una '@'
    if correo.find(" ") != -1 or correo.count("@") != 1:
        return False

    lista = correo.split("@")
    usuario = lista[0]
    dominio = lista[1]

    # El usuario no puede estar vacío
    # El dominio debe tener al menos un punto (find == -1 significa que NO hay punto)
    if usuario == "" or dominio.find(".") == -1:
        return False

    # El dominio no puede empezar en punto (find == 0),
    # ni terminar en punto (dominio[-1] == "."),
    # ni tener puntos seguidos (find("..") != -1)
    if dominio.find(".") == 0 or dominio[-1] == "." or dominio.find("..") != -1:
        return False

    # La extensión final (ej. .com, .es) debe tener al menos 2 letras
    extension = dominio.split(".")[-1]
    if len(extension) < 2 or not extension.isalpha():
        return False

    return True


email = input("Introduce tu correo electrónico: ")

if es_correo_valido(email):
    print("El formato del correo es válido.")
else:
    print("Correo incorrecto. Revisa el formato (ejemplo@dominio.com).")