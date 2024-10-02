
def obtenir_valor1():
    while True:
        try:
            valor = int(input(f"Introdueix el primer valor: "))
            return valor
        except ValueError:
            print("Valor no vàlid. Si us plau, introdueix un número.")
def obtenir_valor2():
    while True:
        try:
            valor = int(input(f"Introdueix el segon valor: "))
            return valor
        except ValueError:
            print("Valor no vàlid. Si us plau, introdueix un número.")


valor1 = obtenir_valor1()  
valor2 = obtenir_valor2()  


if valor1 > valor2:
    print(f"El valor més gran és: {valor1}")
elif valor2 > valor1:
    print(f"El valor més gran és: {valor2}")
else:
    print("Els dos valors són iguals.")
