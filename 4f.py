import random

numero_aleatorio = random.randint(1, 100)
print("¡Adivina el número secreto entre 1 y 100!")

intentos = 0
while True:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1

    if intento == numero_aleatorio:
        print("¡Felicidades! ¡Has adivinado el número secreto en", intentos, "intentos!")
        break
    elif intento < numero_aleatorio:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")