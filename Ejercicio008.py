codigo = input("Ingrese el codigo de producto: ").strip().upper()
if codigo.startswith("PROD-") and len(codigo) == 9 and codigo[5:].isdigit():
    print("Codigo de producto valido.")
elif not codigo.startswith("PROD-"):
    print("Error: El codigo debe empezar con 'PROD-'.")
else:
    print("Error: La parte final debe contener exactamente 4 digitos numericos.")