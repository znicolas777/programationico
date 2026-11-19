bicicletas_disponibles = 40
opcion = 0
bicicletas_arrendadas = 0
bicicletas_devueltas = 0
bicicletas_activas = 0


print("¡Bienvenido al sistema de arriendo de bicicletas de la CicloEstación Campus Verde!")

menu_activo = True
while menu_activo:
    print("---------- MENU PRINCIPAL ----------")
    print("1. Bicicletas disponibles")
    print("2. Realizar el arriendo")
    print("3. Devolver el arriendo")
    print("4. Historial de arriendos")
    print("5. Salir")
    print(" -----------------------------------")
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion <= 0:
            print("Debe ingresar un numero entero positivo del 1 al 5")
        else:
            if opcion == 1:
                print(f"bicicletas disponibles: {bicicletas_disponibles}")
            elif opcion == 2:
                cantidad_valida = False
                while not cantidad_valida:
                    try:
                        cantidad_arrendar_bicicletas = int(input("Ingrese cuantas bicicletas desea arrendar: "))
                        if cantidad_arrendar_bicicletas <= 0:
                            print("debe ser un numero entero positivo mayor a 0: ")
                        elif cantidad_arrendar_bicicletas > bicicletas_disponibles:
                            print("no puedes arrendar mas bicis de las disponibles")
                        else:
                            bicicletas_disponibles = bicicletas_disponibles - cantidad_arrendar_bicicletas
                            bicicletas_arrendadas = bicicletas_arrendadas + cantidad_arrendar_bicicletas 
                            bicicletas_activas = bicicletas_activas + cantidad_arrendar_bicicletas
                            cantidad_valida = True
                    except ValueError:
                        print("Ingrese un numero entero no letras")
            elif opcion == 3:
                cantidad_valida = False
                while not cantidad_valida:
                    try:
                        cantidad_devolver_bicicletas = int(input("Ingrese la cantidad a devolver de bicicletas: "))
                        if cantidad_devolver_bicicletas <= 0:
                            print("Debe ingresar un numero entero positivo mayor a 0")
                        elif cantidad_devolver_bicicletas > bicicletas_activas:
                            print("La cantidad a devolver no puede ser mayor a las bicicletas activas")
                        else:
                            bicicletas_disponibles = bicicletas_disponibles + cantidad_devolver_bicicletas
                            bicicletas_devueltas = bicicletas_devueltas + cantidad_devolver_bicicletas
                            bicicletas_activas = bicicletas_activas - cantidad_devolver_bicicletas
                            cantidad_valida = True
                    except ValueError:
                        print("Ingrese un numero entero no letras")         
            elif opcion == 4:
                print("----- HISTORIAL -----")
                print(f"total de bicicletas arrendadas: {bicicletas_arrendadas}")
                print(f"total de bicicletas devueltas: {bicicletas_devueltas}")
                print(f"total de bicicletas activas: {bicicletas_activas}")
                
            elif opcion == 5:
                print("Gracias por utilizar nuestro software, hasta la próxima.")
                menu_activo = False
            else:
                print("Debe seleccionar una opcion del 1 al 5")
    except ValueError:
        print("Ingrese un numero entero no letras")
    
