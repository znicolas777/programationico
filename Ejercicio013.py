num1 = int(input("Ingrese el limite inferior: "))
num2 = int(input("Ingrese el limite superior: "))

from random import randint

numero_aleatorio = randint(num1, num2)

ajustado = (numero_aleatorio // 3) * 3

if ajustado < num1:
    ajustado = num1

intento1 = int(input("Ingrese el numero: "))

if intento1 == ajustado:
    print("¡¡¡¡ FELICIDADES LO ADIVINASTE A LA PRIMERA !!!!")

else:
    if intento1 < ajustado:
        print("El numero es mayor")
    else:
        print("El numero es menor")

    intento2 = int(input("Ingrese el numero: "))

    if intento2 == ajustado:
        print("¡¡ Lo adivinaste en el segundo intento !!")

    else:
        if intento2 < ajustado:
            print("El numero es mayor")
        else:
            print("El numero es menor")

        distancia_intento1 = abs(ajustado - intento1)
        distancia_intento2 = abs(ajustado - intento2)

        if distancia_intento1 < distancia_intento2:
            print(f"El numero esta mas cerca de {intento1}")
        else:
            print(f"El numero esta mas cerca de {intento2}")

        intento3 = int(input("Ingrese el numero: "))

        if intento3 == ajustado:
            print("¡¡ Lo adivinaste en el tercer intento !!")
        else:
            print("Perdiste.")
            print(f"El numero era: {ajustado}")
