def menu():
    print("1. ")
    print("2. Salir")

cantidad_valida = False
analistas = 0
gerentes= 0
antiguedad = 0
codigo_empleado = ""

while not cantidad_valida:
    try:
        num_ejecutivos = int(input("Ingrese la cantidad de ejecutivos: "))
        cantidad_valida = num_ejecutivos > 0

        if not cantidad_valida:
            print("transaccion invalida, ingrese un numero entero positivo")

    except ValueError:
        print("Debe ingresar un numero entero no letras")

for i in range(num_ejecutivos):
    valido = False
    while not valido:
        codigo_empleado = input("Ingrese el codigo del empleado: ").strip()
        valido = len(codigo_empleado) >= 6 and not " " in codigo_empleado

        if not valido:
            print("el codigo no es valido, intente nuevamente")

    valido = False
    while not valido:
        try:
            antiguedad = int(input("Ingrese los años de antiguedad: "))
            valido = antiguedad > 0

            if not valido:
                print("la antiguedad no es valida debe ingresar un numero entero positivo")
        except ValueError:
            print("Debe ingresar un numero entero positivo no letras")

    if antiguedad >3:
        gerentes = gerentes + 1
    else:
        analistas = analistas + 1

print(f"la oficina cuenta con {gerentes} gerentes y {analistas} analistas")