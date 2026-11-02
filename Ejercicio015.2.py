edad = int(input("Ingrese la edad: "))
tramo = input("Ingrese el tramo: ").lower()

if edad <= 30 and tramo == "a" or edad <= 30 and tramo == "b":
    descuento = 0.18
elif edad <= 30 and tramo == "c" or edad <= 30 and tramo == "d":
    descuento = 0.12

if edad <= 31 and edad <= 60 and tramo == "a" or edad <= 31 and edad <= 60 and tramo == "b":
    descuento = 0.12
elif edad <= 31 and edad <= 60 and tramo == "c" or edad <= 31 and edad <= 60 and tramo == "d":
        descuento= 0.08

print(f"descuento final es: {descuento}")