edad = int(input("Ingrese la edad: "))
tramo = input("Ingrese el tramo: ").lower()

if edad <= 30:
    if tramo == "a" or tramo == "b":
        descuento = 0.18
    elif tramo == "c" or tramo == "d":
        descuento = 0.12

if edad <= 31 and edad <= 60:
    if tramo == "a" or tramo == "b":
        descuento = 0.12
    elif tramo == "c" or tramo == "d":
        descuento= 0.08

print(f"descuento final es: {descuento}")