def calcula_factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def main():
    num = int(input("Inserta un entero para factorizar: "))
    if num < 0:
        print("No se pueden insertar números negativos.")
    else:
        fact = calcula_factorial(num)
        print("El factorial de", num, "es:", fact)

if __name__ == "__main__":
    main()
