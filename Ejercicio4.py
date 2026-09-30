nombre = input("ingrese el nombre: ")
if nombre == "":
    print("El nombre no puede estar vacio")
elif nombre.islower or nombre.isupper():
    nombre_formateado = nombre.title()
    print(f"nombre formateado: {nombre_formateado} ")
else:
    print(f"nombre correcto: {nombre} ")
