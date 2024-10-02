input = input("Introdueix 2 paraules: ")

words = input.split()

if len(words) != 2:
    print("Error: Has d'introduir 2 paraules.")
else:
    for word in words:
        firstWord = words[0]
        secondWord = words[1]

        firstWord2 = secondWord[:2] + firstWord[2:]
        secondWord2 = firstWord[:2] + secondWord[2:]

    print(f"Resultat: {firstWord2} {secondWord2}")