import random

escoge_maquina = random.randint(1, 3)

def opciones(numero):
    if numero == 1  and escoge_maquina ==1 :
        return"empate"
    elif numero == 1 and escoge_maquina ==2:
        return "gana maquina"
    elif numero == 1 and escoge_maquina ==3:
        return "gana jugador"
    if numero == 2  and escoge_maquina ==1 :
        return"gana jugador"
    elif numero == 2 and escoge_maquina ==2:
        return "empate"
    elif numero == 2 and escoge_maquina ==3:
        return "gana maquina"
    if numero == 3  and escoge_maquina ==1 :
        return"gana maquina"
    elif numero == 3 and escoge_maquina ==2:
        return "gana jugador"
    elif numero == 3 and escoge_maquina ==3:
        return "empate"
    else:
        return "opcion incorrecta"

print("Ingresa una opcion")
print("1 = piedra")
print("2 = papel")
print("3 = tijera")
numero = int(input(""))

opcion = opciones(numero)

print(f" {opcion}.")

