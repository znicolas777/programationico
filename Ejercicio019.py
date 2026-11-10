citas_disponibles = 40
citas_programadas = 0
citas_canceladas = 0

def menu():
    print("---------- MENU PRINCIPAL ----------")
    print("1. citas disponibles")
    print("2. programar citas")
    print("3. cancelar citas")
    print("4. historial de citas")
    print("5. salir")
    print("------------------------------------")

print("bienvenido a la clinica los cachorros")

while True:
    menu()

    try:
        opcion = int(input("Ingrese una opcion: ").strip())
    except ValueError:
        print("debe ingresar numeros no letras")
        continue

    if opcion == 1:
        print(f"las citas disponibles son: {citas_disponibles}")

    elif opcion == 2:
        valido = False

        while not valido:
            try:
                cantidad_cita = int(input("Ingrese cuantas citas desea programar: "))

                if cantidad_cita > citas_disponibles:
                    print("no hay citas disponibles")
                elif cantidad_cita <= 0:
                    print("el numero de citas debe ser mayor a 0")
                else:
                    citas_programadas = citas_programadas + cantidad_cita
                    citas_disponibles = citas_disponibles - cantidad_cita
                    valido = True

            except ValueError:
                print("debe ingresar numeros no letras")

    elif opcion == 3:
        valido = False

        while not valido:
            try:
                cancelar_cita = int(input("Cuantas citas desea cancelar: "))

                if cancelar_cita > citas_programadas:
                    print("el numero a cancelar no puede ser mayor a las citas programadas")
                elif cancelar_cita <= 0:
                    print("el numero de citas debe ser mayor a 0")
                else:
                    citas_canceladas = citas_canceladas + cancelar_cita
                    citas_programadas = citas_programadas - cancelar_cita
                    citas_disponibles = citas_disponibles + cancelar_cita
                    valido = True

            except ValueError:
                print("debe ingresar un numero entero, no letras")

    elif opcion == 4:
        print("----- historial citas -----")
        print(f"citas programadas: {citas_programadas}")
        print(f"citas canceladas: {citas_canceladas}")
        print(f"citas disponibles: {citas_disponibles}")

    elif opcion == 5:
        print("gracias por usar el programa")
        break

    else:
        print("debe ingresar una opcion valida del (1 a 5)")
