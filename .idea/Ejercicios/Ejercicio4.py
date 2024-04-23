import random
import string

def genera_password(dimension):
    simbolos = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(simbolos) for i in range(dimension))
    return password

def main():
    dimension = int(input("Inserta la dimensión de la password: "))
    password = genera_password(dimension)
    print("Esta es tú password:", password)

if __name__ == "__main__":
    main()
