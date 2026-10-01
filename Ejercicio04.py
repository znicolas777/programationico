correo = input("Ingrese su correo: ")
if correo.count("@") == 1 and not correo.startswith("@") and (correo.endswith(".com") or correo.endswith(".org")):
    print("Correo validado")
elif not correo.count("@") == 1:
    print("solo puede contener un @")
else:
    print("El correo debe terminar en .com o .org y no empezar con @")