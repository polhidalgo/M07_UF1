def obtenirValor():
    while True:
        try:
            valor=(float(input("Introdueix valor: ")))
            return valor
        except ValueError:
            print("Valor no valid")
            
def obtenirIva():
    while True: 
        try:
            iva = (int(input("ntrodueix '%' de IVA(4%, 10%, 21%):  ")))
            if iva in [4,10,21]:
                return iva
            else:
                print("IVA no vàlid. Si us plau, introdueix 4, 10 o 21.")
        except ValueError:
            print("Valor no vàlid. Si us plau, introdueix un número.")
def calcularFinal(valor, iva):
    valorIva = valor * (1 + (iva / 100))
    return valorIva

valor = obtenirValor()
iva = obtenirIva()

valorFinal = calcularFinal(valor, iva)

print(f"Valor inicial: {valor} €")
print(f"Percentatge d'IVA: {iva}%")
print(f"Valor final amb IVA: {valorFinal:.2f} €")