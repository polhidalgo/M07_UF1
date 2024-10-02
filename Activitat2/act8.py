
inputUser = input("Introdueix entre 1 i 3 paraules separades per espais: ")

words = inputUser.split()

if len(words) < 1 or len(words) > 3:
    print("Error: Has d'introduir entre 1 i 3 paraules.")
else:
    for word in words:
        numeroCaracters = len(word)
        primerCaracter = word[0]
        ultimCaracter = word[-1]

        print(f"Paraula: {word}")
        print(f"Nombre de caràcters: {numeroCaracters}")
        print(f"Primer caràcter: {primerCaracter}")
        print(f"Últim caràcter: {ultimCaracter}")