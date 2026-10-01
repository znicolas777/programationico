contrasena = input("Ingrese la contraseña: ")
if len(contrasena) >= 8 and not contrasena.isalpha() and not contrasena.isnumeric() and not contrasena.find(" ") == -1 :
    print("contraseña fuerte")
elif len(contrasena) < 8:
    print("la contraseña debe tener al menos 8 caracteres")
elif contrasena.isalpha() or contrasena.isnumeric():
    print("la contraseña debe ser alfanumerica")
else:
    print("La contraseña no puede contener espacios en blanco")