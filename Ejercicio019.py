nombre = input("Ingrese el nombre: ")
especie = input("Ingrese la especie: ")
urgencia = int(input("Ingrese el nivel de urgencia: "))
atendido =  False

diccionario = {
    "nombre":  nombre,
    "especie": especie,
    "urgencia": urgencia,
    "atendido": False
}

atenciones = {
}

atenciones.append(diccionario)