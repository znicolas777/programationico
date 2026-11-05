def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Salir")

menu()
try:    
    opcion = int(input("Ingrese una opcion: "))
except ValueError:
    print("no se permiten letras en la opcion, intente nuevamente")
else:
    while opcion != 5:
        num1 = 0
        num2 = 0
        resultado = 0
        if opcion == 1:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("solo ingresar numeros")
            else:
                resultado = num1 + num2
                print(f"el resultado de la suma es: {resultado}")
        elif opcion == 2:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("solo ingresar numeros")
            else:
                resultado = num1 - num2
                print(f"el resultado de la resta es: {resultado}")
        elif opcion == 3:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("solo ingresar numeros")
            else:
                while num2 == 0:
                    print("no se puede dividir por 0")
                    opcion = int(input("Ingrese una opcion: "))
                resultado = num1 / num2
                resultado = (round(resultado,2))
                print(f"el resultado de la division es: {resultado}")
        elif opcion == 4:
            try:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
            except ValueError:
                print("solo ingresar numeros")
            else:
                resultado = num1 * num2
                print(f"el resultado de la multiplicacion es: {resultado}")
        elif opcion == 5:
            print("gracias por usar la calculadora")
        else:
            print("debe selecionar una opcion del (1 al 5): ")

        menu()

        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("debe ser un numero entero no letras")