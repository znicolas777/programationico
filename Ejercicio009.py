nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip()
if nombre.isalpha() and apellido.isalpha() and len(nombre) > 0 and len(apellido) > 0:
    usuario_generado = (nombre[0] + apellido).lower()
    print(f"Su nombre de usuario es: {usuario_generado}")
elif nombre == "" or apellido == "":
    print("Error: Debe ingresar ambos datos.")
else:
    print("Error: El nombre y apellido solo deben contener letras.")