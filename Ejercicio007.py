comentario = input("Ingrese su comentario: ")
if comentario.strip() == "":
    print("El comentario no puede estar vacio.")
elif "tonto" in comentario.lower() or "feo" in comentario.lower():
    comentario_limpio = comentario.replace("tonto", "*****").replace("feo", "***")
    print(f"Comentario censurado: {comentario_limpio}")
else:
    print(f"Comentario publicado: {comentario}")