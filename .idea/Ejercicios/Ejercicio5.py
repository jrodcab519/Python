import random

def adivina_numero():
    num_random = random.randint(1, 100)

    while True:
        oportunidad = int(input("Inserta un número del 0 al 100: "))

        if oportunidad < num_random:
            print("El número que debes adivinar es mayor.")
        elif oportunidad > num_random:
            print("El número que debes adivinar es menor.")
        else:
            print("Acertaste, Enhorabuena")
            break
adivina_numero()

