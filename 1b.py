numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))


if numero1 > numero2:
    print(f"{numero1} es el número más grande.")
elif numero2 > numero1:
    print(f"{numero2} es el número más grande.")
else:
    print("Los números son iguales.")