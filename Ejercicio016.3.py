def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Salir")

opcion = 0
while opcion != 5:
    menu()
    try:    
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("no se permiten letras en la opcion, intente nuevamente")
        continue

    num1 = 0
    num2 = 0
    resultado = 0

    match opcion:
        case 1:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("debe ingresar numeros enteros no letras")
            else: 
                resultado = num1 + num2
                print(f"el resultado de la suma es: {resultado}")
        case 2:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("debe ingresar un numeros enteros no letras")
            else:
                resultado = num1 - num2
                print(f"el resultado de la resta es: {resultado}")
        case 3:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("debe ingresar numeros enteros no letras")
            else:
                while num2 == 0:
                    print("no se puede dividir por 0")
                    opcion = int(input("Ingrese una opcion: "))
                resultado = num1 / num2
                resultado = (round(resultado,2))
                print(f"el resultado de la division es: {resultado}")
        case 4:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                    print("debe ingresar numeros enteros no letras")
            else:
                resultado = num1 * num2
                print(f"el resultado de la multiplicacion es: {resultado}")
        case 5:
            print("programa finalizado.")
            print("gracias por usar el programa")
            break
        case _:
            print("debe ingresar una opcion del (1 al 5): ")

    menu()

    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
            print("debe ser un numero entero no letras")