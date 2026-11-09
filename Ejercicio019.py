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
        opcion = int(input("Igrese una opcion: ").strip())
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
                valido = cantidad_cita > 0 and cantidad_cita <= citas_disponibles
            except ValueError:
                print("debe ingresar numeros no letras")

                if not valido and cantidad_cita > citas_disponibles:
                    print("no hay citas disponibles")
                elif not valido:
                    print("el numero de visitas debe ser mayor a 0")
                else:
                    citas_programadas = citas_programadas + cantidad_cita
                    citas_disponibles = citas_disponibles - cantidad_cita

    elif opcion == 3:
        valido = False
        while not valido:
            try:
                cancelar_cita = int(input("Cuantas citas desea cancelar: "))
                valido = cancelar_cita > 0 and cancelar_cita <= cantidad_cita
            except ValueError:
                print("debe ser un numero entero no letras")

                if not valido and cantidad_cita < cancelar_cita:
                    print("el numero a cancelar no puede ser mayor")
                elif not valido:
                    print("el numero de visitas debe ser mayor a 0")
                else:
                    citas_canceladas = citas_canceladas + cantidad_cita
                    citas_disponibles = citas_disponibles + cantidad_cita
        
            


    elif opcion == 4:
        citas_programadas = cantidad_cita
        citas_canceladas = cancelar_cita
        print("----- historial citas -----")
        print(f"citas programadas {citas_programadas}")
        print(f"citas canceladas {citas_canceladas}")

    elif opcion == 5:
        print("gracias por usar el programa")
        break
    else:
        print("debe ingresar una opcion valida del (1 a 5)")