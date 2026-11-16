# --- FUNCIONES DE VALIDACIÓN ---
def validad_nombre(nombre):
    return len(nombre.strip()) > 0

def validar_especie(especie):
    return especie.lower().strip() in ["perro", "gato", "huron"]

def validar_urgencia(urgencia_str):
    if urgencia_str.strip().isdigit():
        urgencia = int(urgencia_str.strip())
        return 1 <= urgencia <= 5
    return False

# --- FUNCIONES AUXILIARES ---
def buscar_indice_pacientes(nombres, nombre_buscado):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscado.lower().strip():
            return i
    return -1

def mostrar_menu():
    print("\n---------- HOSPITAL VETERINARIO ----------")
    print("1. Ingresar nuevo paciente")
    print("2. Atender siguiente emergencia")
    print("3. Buscar paciente por nombre")
    print("4. Dar de alta")
    print("5. Mostrar todos los pacientes")
    print("6. Salir")
    print("------------------------------------------")

# --- FUNCIONES DEL SISTEMA ---
def ingresar_paciente(nombres, especies, urgencias, atendidos):
    print("------- Ingreso de paciente -------")
    nombre = input("Nombre de mascota: ")
    if not validad_nombre(nombre):
        print("Error, el nombre no puede estar vacío")
        return

    if buscar_indice_pacientes(nombres, nombre) != -1:
        print("Error: ya existe un paciente registrado con ese nombre")
        return

    especie = input("Especie (perro / gato / huron): ")
    if not validar_especie(especie):
        print("Error: especie no válida. Debe ingresar perro / gato / huron")
        return

    urgencia_str = input("Nivel de urgencia: (1 = leve, 5 = crítico) ").strip()
    if not validar_urgencia(urgencia_str):
        print("Error, urgencia debe estar entre los valores 1 a 5")
        return

    nombres.append(nombre.strip().capitalize())
    especies.append(especie.strip().capitalize())
    urgencias.append(int(urgencia_str))
    atendidos.append(False) # Siempre entra como False (en espera)
    print(f"Paciente {nombre.strip().capitalize()} registrado en sala de espera.")

def atender_emergencia(nombres, especies, urgencias, atendidos):
    print("\n Llamado a Consulta")
    indice_prioritario = -1
    mayor_urgencia = 0

    # Recorremos todas las listas buscando el no atendido con mayor urgencia
    for i in range(len(nombres)):
        if not atendidos[i] and urgencias[i] > mayor_urgencia:
            mayor_urgencia = urgencias[i]
            indice_prioritario = i

    if indice_prioritario == -1:
        print("No hay pacientes pendientes en sala de espera.")
    else:
        atendidos[indice_prioritario] = True
        print(f"Atendiendo a: {nombres[indice_prioritario]} ({especies[indice_prioritario]}) - Urgencia: {urgencias[indice_prioritario]}")

def buscar_paciente(nombres, especies, urgencias, atendidos):
    print("\n------- Buscar Paciente -------")
    nombre = input("Ingrese el nombre del paciente a buscar: ")
    indice = buscar_indice_pacientes(nombres, nombre)

    if indice == -1:
        print("Paciente no encontrado.")
    else:
        estado = "Atendido" if atendidos[indice] else "En espera"
        print(f"Paciente: {nombres[indice]} | Especie: {especies[indice]} | Urgencia: {urgencias[indice]} | Estado: {estado}")

def dar_de_alta(nombres, especies, urgencias, atendidos):
    print("\n------- Dar de Alta -------")
    nombre = input("Ingrese el nombre del paciente a dar de alta: ")
    indice = buscar_indice_pacientes(nombres, nombre)

    if indice == -1:
        print("Paciente no encontrado.")
    elif not atendidos[indice]:
        print("Error: el paciente aún está en sala de espera y no ha sido atendido.")
    else:
        eliminado = nombres.pop(indice)
        especies.pop(indice)
        urgencias.pop(indice)
        atendidos.pop(indice)
        print(f"Paciente {eliminado} dado de alta exitosamente.")

def mostrar_todos(nombres, especies, urgencias, atendidos):
    print("\n------- Registro de Pacientes -------")
    if len(nombres) == 0:
        print("No hay pacientes registrados.")
        return

    for i in range(len(nombres)):
        estado = "Atendido" if atendidos[i] else "En espera"
        print(f"{i+1}. {nombres[i]} ({especies[i]}) - Urgencia: {urgencias[i]} - [{estado}]")

# --- PROGRAMA PRINCIPAL ---
def main():
    nombres = []
    especies = []
    urgencias = []
    atendidos = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ingresar_paciente(nombres, especies, urgencias, atendidos)
        elif opcion == "2":
            atender_emergencia(nombres, especies, urgencias, atendidos)
        elif opcion == "3":
            buscar_paciente(nombres, especies, urgencias, atendidos)
        elif opcion == "4":
            dar_de_alta(nombres, especies, urgencias, atendidos)
        elif opcion == "5":
            mostrar_todos(nombres, especies, urgencias, atendidos)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
main()