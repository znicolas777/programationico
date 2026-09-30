usuario = input("Ingrese el nombre de usuario: ")
if len(usuario) > 5 and len(usuario) < 15 and usuario[0].isalpha() and usuario.isalnum():
    print("nombre de usuario valido")
elif len(usuario) <= 5 or len(usuario) >= 15:
    print("error, la longitud debe estar entre 5 a 15 caracteres")
else:
    print("error, el usuario debe ser alfanumerico y empezar con letra")