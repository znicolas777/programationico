contraseña = input("Ingrese la contraseña: ")

if len(contraseña) >= 8 and not contraseña.isalpha() and not contraseña.isnumeric() and contraseña.fiind(""== 1):
    print("La contraseña es fuerte")
elif len(contraseña) < 8:
    print("contraseña demasiada corta")
else:
    print("la contraseña debe incluir letras y numeros y no tener espacios")