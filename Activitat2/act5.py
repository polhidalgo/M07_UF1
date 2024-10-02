
def obtenir_numero():
    while True:
        try:
            numero = int(input("Introdueix un numero enter: "))
            return numero
        except ValueError:
            print("Valor no valid.")


numero = obtenir_numero()

if numero % 2 == 0:
    print(f"El numero {numero} es parell.")
else:
    print(f"El numero {numero} es senar.")
