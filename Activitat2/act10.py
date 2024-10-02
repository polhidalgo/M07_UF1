import random

secretNumber = random.randint(1, 100)

intents = 0

print("adivina el numero entre 1 i 100")

while True:
    game = int(input("Introdueix el numero: "))

    intents += 1

    if game < secretNumber:
        print("El numero es mes gran")
    elif game > secretNumber:
        print("El numero es mes petit")
    else:
        print(f"El numero es: {secretNumber}")
        print(f"Intents: {intents}")
        break