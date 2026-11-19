profesional_titular = 0
promesa_cantera = 0

valido = False


while not valido:
    try:
        cantidad_futbolistas = int(input("Ingrese cuantos futbolistas desea ingresar: "))
        if cantidad_futbolistas <= 0:
            print("¡Ficha de inscripción inválida! Ingresa un entero positivo para continuar.")
        else:
            valido = True
    except ValueError:
        print("Debe ingresar un numero entero no letras")



for i in range(cantidad_futbolistas):
    alias_valido = False
    while not alias_valido:
            alias_deportivo = input("Ingrese el alias deportivo: ").strip()
            if len(alias_deportivo) >= 6 and " " not in alias_deportivo:
                alias_valido = True
            else:
                print("El alias deportivo debe tener como minimo 6 caracteres")
    anios_valido = False
    while not anios_valido: 
        try:
            años_jugados = int(input("Ingrese cuantos años ah jugado: "))
            if años_jugados <= 0:
                            print("¡Error de cancha! Ingresa un número entero positivo para los años jugados")
            elif años_jugados > 5:
                profesional_titular = profesional_titular + 1
                anios_valido = True
            else:
                promesa_cantera = promesa_cantera + 1  
                anios_valido = True  
        except ValueError:
            print("Debe ingresar un numero entero no letras")

print(f"el club cuenta con {profesional_titular} profesionales titulares y {promesa_cantera} promesas de cantera")
                



