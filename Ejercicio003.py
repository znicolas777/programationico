nombre = input("Ingrese su nombre: ")
if nombre == " ":
    print("El nombre no puede estar vacio")
elif nombre.islower() or nombre.isupper():
    nombre_nuevo = nombre.title()
    print(f"su nombre cambiado es: {nombre_nuevo}")
else:
    print(f"su nombre es: {nombre}")

    
