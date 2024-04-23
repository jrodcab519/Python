def cuenta_palabras(frase):
    frase = frase.strip()

    if not frase:
        return 0

    palabras = frase.split()

    return len(palabras)

def main():
    frase = input("Inserta una frase:\n")
    numero_palabras = cuenta_palabras(frase)
    print("Palabras:", numero_palabras)

if __name__ == "__main__":
    main()

