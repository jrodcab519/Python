def valida_password(password):
    caracteres_minimos = 8
    mayuscula = False
    minuscula = False
    numero = False

    if len(password) < caracteres_minimos:
        return False

    for caracter in password:
        if caracter.isupper():
            mayuscula = True
        elif caracter.islower():
            minuscula = True
        elif caracter.isdigit():
            numero = True

    return mayuscula and minuscula and numero

def main():
    password = input("Inserta una password: ")
    if valida_password(password):
        print("La password cumple los requisitos.")
    else:
        print("La password no cumple los requisitos.")

if __name__ == "__main__":
    main()
