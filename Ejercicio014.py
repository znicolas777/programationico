membresia_mensual = 150_000
casillero = 15_000

asistencia = int(input("Ingrese la cantidad de dias de asistencia al mes (0 a 30):  "))
categoria = input("Ingrese la categoria (vip.premium,estandar,basica): ").lower().strip()

if asistencia >= 20:
    if categoria == "vip" or categoria == "premium":
        descuento_membresia = 0.25
    elif categoria == "estandar" or categoria == "basica":
        descuento_membresia = 0.15
elif asistencia >= 12 and asistencia <= 19:
    if categoria == "vip" or categoria == "premium":
        descuento_membresia = 0.12
    elif categoria == "estandar" or categoria == "basica":
        descuento_membresia = 0.08
elif asistencia < 12:
    if categoria == "estandar" or categoria == "basica" or categoria == "vip" or categoria == "premium":
        descuento_membresia = 0
else:
    print("ingrese un valor valido")

if categoria == "vip" or categoria == "premium":
    descuento_casillero = 0.10
    if asistencia >= 15:
        descuento_casillero = 0.15
elif categoria == "estandar" or categoria == "basica":
    descuento_casillero = 0
else:
    print("ingrese un valor valido")

valor_membresia = membresia_mensual - (membresia_mensual * descuento_membresia)
valor_casillero = casillero - (casillero * descuento_casillero)

print(f"el valor de la membresia es: {valor_membresia}")
print(f"el valor del casillero es: {valor_casillero}")