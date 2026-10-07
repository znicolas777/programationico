email = input("ingrese su email: ").lower().strip()
valido = False
for caracter in email:
    if caracter == "@":
        valido = True
        print("El correo es valido")
        break
if valido is not True:
    print("correo invalido")