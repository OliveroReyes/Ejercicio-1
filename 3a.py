import random

numero_secreto = random.randint(1, 50)

print("Bienvenido al juego de adivinar el número secreto")
print("Intenta adivinar el número secreto generado entre 1 y 50.")


intentos = 0


while True:
    
    intento = int(input("Ingresa tu intento: "))
    
    intentos += 1
    
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
        break 