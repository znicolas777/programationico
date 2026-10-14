pasaje_mensual = 95000
emision_tarjeta = 5000 

distancia = int(input("Ingrese la distancia en km: "))

categoria = int(input("Ingrese la categoria del (1 al 5):  "))

if distancia >= 400:
    if categoria == 1 or categoria == 2:
        descuento_pasaje = 0.20
    elif categoria == 3 or categoria == 4:
        descuento_pasaje = 0.14
    else:
        descuento_pasaje = 0
        print("opcion no valida ingrese nuevamente")

elif distancia >= 200 and distancia < 400:
    if categoria == 1 or categoria == 2:
        descuento_pasaje = 0.12
    elif categoria == 3 or categoria == 4:
        descuento_pasaje = 0.08
    else:
        descuento_pasaje = 0
        print("opcion no valida intente denuevo")

valor_pasaje = int(95_000 * (1 - descuento_pasaje))


descuento_tarjeta = 0
if categoria == 1 or categoria == 2 or categoria == 3:
    descuento_tarjeta = 0.10
    if distancia >= 300:
        descuento_tarjeta = 0.15

valor_tarjeta = int(5_000 * (1 - descuento_tarjeta))

print(f"el valor del pasaje es: {valor_pasaje}")
print(f"el valor de la tarjeta es: {valor_tarjeta}")