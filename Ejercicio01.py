usuario = input("Ingrese su usuario: ")
if len(usuario) > 5 and len(usuario) < 15 and usuario[0].isalpha() and usuario.isalnum():
    print("buen nombre de usuario")
elif len(usuario) <= 5 and len(usuario) >= 15:
    print("El usuario debe tener entre 6 a 14 caracteres")
else:
    print("error, mal nombre de usuario")