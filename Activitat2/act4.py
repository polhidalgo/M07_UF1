

def obtenir_valor1():
    while True:
        try:
            valor = int(input(f"Introdueix el primer valor: "))
            return valor
        except ValueError:
            print("Valor no valid.")
def obtenir_valor2():
    while True:
        try:
            valor = int(input(f"Introdueix el segon valor: "))
            return valor
        except ValueError:
            print("Valor no valid.")
def obtenir_operacio():
    while True:
        operacio = input("Introdueix l'operació a realitzar (suma, resta, divisio, multiplicacio): ").strip().lower()
        if operacio in ["suma", "resta", "divisió", "multiplicació"]:
            return operacio
        else:
            print("Operació no vàlida. Si us plau, escull entre: suma, resta, divisió, multiplicació.")
            
valor1 = obtenir_valor1()  
valor2 = obtenir_valor2()  
operacio = obtenir_operacio()

if operacio == "suma":
    resultat = valor1 + valor2
    print(f"El resultat de la suma és: {resultat}")
elif operacio == "resta":
    resultat = valor1 - valor2
    print(f"El resultat de la resta és: {resultat}")
elif operacio == "multiplicació":
    resultat = valor1 * valor2
    print(f"El resultat de la multiplicació és: {resultat}")
elif operacio == "divisió":
    # Comprovar que no es faci una divisió per zero
    if valor2 != 0:
        resultat = valor1 / valor2
        print(f"El resultat de la divisió és: {resultat}")
    else:
        print("Error: No es pot dividir per zero.")