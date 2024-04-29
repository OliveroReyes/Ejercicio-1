import random

def generar_palabra():
    palabras = ["casa", "perro", "gato", "computadora", "python", "programacion", "avion", "universidad"]
    return random.choice(palabras)

def ocultar_letras(palabra):
    oculta = ""
    for _ in palabra:
        oculta += "_"
    return oculta

def mostrar_palabra(oculta):
    for letra in oculta:
        print(letra, end=" ")
    print()

def jugar():
    palabra = generar_palabra()
    oculta = ocultar_letras(palabra)
    intentos = len(palabra)
    while "_" in oculta and intentos > 0:
        mostrar_palabra(oculta)
        letra = input("Ingresa una letra: ")
        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue
        acierto = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                oculta = oculta[:i] + letra + oculta[i+1:]
                acierto = True
        if acierto:
            print("¡Bien! Has acertado una letra.")
        else:
            print("Letra incorrecta. Inténtalo de nuevo.")
            intentos -= 1
    if "_" not in oculta:
        print("¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("¡Has agotado todos los intentos! La palabra era:", palabra)

if __name__ == "__main__":
    jugar()