pasaje_mensual = 95000
emision_tarjeta = 5000
descuento_tarjeta = 0
descuento_pasaje = 0

distancia = int(input("Ingrese la distancia en km: "))

categoria = int(input("Ingrese la categoria del (1 al 5):  "))


if distancia >= 400 and (categoria == 1 or categoria == 2):
    descuento_pasaje = pasaje_mensual - (pasaje_mensual * 0.20) 
elif distancia >= 400 and (categoria == 3 or categoria == 4):
    descuento_pasaje = pasaje_mensual - (pasaje_mensual * 0.14)
elif distancia >= 200 and distancia < 400 and (categoria == 1 or categoria == 2):
    descuento_pasaje = pasaje_mensual - (pasaje_mensual * 0.12)
elif distancia >= 200 and distancia < 400 and (categoria == 3 or categoria == 4):
    descuento_pasaje = pasaje_mensual - (pasaje_mensual * 0.08)
else:
    descuento_pasaje = pasaje_mensual

if categoria in (1, 2 , 3) and distancia >= 300:
    descuento_tarjeta = emision_tarjeta - (emision_tarjeta * 0.15 )
elif categoria == 1 or categoria == 2 or categoria == 3:
    descuento_tarjeta = emision_tarjeta - (emision_tarjeta * 0.10 )
else:
    descuento_tarjeta = emision_tarjeta

print(f"el valor del pasaje es: {descuento_pasaje}")
print(f"el valor de la tarjeta es: {descuento_tarjeta}")

# pasaje_mensual = 95000 emision_tarjeta = 5000 

if distancia >= 400:
    if categoria == 1 or categoria == 2:
        descuento_pasaje = 0.20
    elif categoria == 3 or categoria == 4:
        descuento_pasaje = 0.14
    else:
        descuento_pasaje = 0
        print("opcion no controlada ingrese nuevamente")

elif distancia >= 200 and distancia < 400:
    if categoria == 1 or categoria == 2:
        descuento_pasaje = 0.12
    elif categoria == 3 or categoria == 4:
        descuento_pasaje = 0.08
    else:
        descuento_pasaje = 0
        print("opcion no valida intente denuevo")
