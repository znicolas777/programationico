palabra = "ingenieria en informatica"
contador = 0

for letra in palabra:
    if letra == " ":
        contador = contador +1
print(f"la cantidad de espacios es: {contador}")