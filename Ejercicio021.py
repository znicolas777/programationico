#LISTA
peliculas = []

while True:
    nombre = input("Ingrese el nombre de la pelicula: ").strip().lower()
    anio = int(input("Ingrese el año de la pelicula: ").strip())
    categoria = input("Ingrese la categoria de la pelicula: ").strip().lower()

    #DICCIONARIO "NOMBRE",CLAVE
    pelicula = {
        "nombre":nombre,
        "año":anio,
        "categoria":categoria

    }

    peliculas.append(pelicula)

    for indice,pelicula in enumerate(peliculas):
        print(f"{indice + 1} " ,pelicula['nombre'].title())
        print(f"{indice + 1} " ,pelicula['año'])
        print(f"{indice + 1} " ,pelicula['categoria'].capitalize())
        print("--------------------")

    print("Desea continuar")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        break