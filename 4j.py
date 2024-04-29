import random

def generar_palabras():
    palabras = ["casa", "perro", "gato", "computadora", "python", "programacion", "avion", "universidad"]
    return palabras

def ocultar_palabra(palabra):
    oculta = "_" * len(palabra)
    return oculta

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def jugar_adivinanzas(palabras):
    print("Bienvenido al juego de adivinanzas")
    palabra = random.choice(palabras)
    letras_adivinadas = set()
    print("La palabra tiene {} letras:".format(len(palabra)))
    palabra_oculta = ocultar_palabra(palabra)
    print(palabra_oculta)
    
    while True:
        if palabra_oculta == palabra:
            print("Felicidades, Has adivinado la palabra correctamente. Has ganado")
            return True

        letra_usuario = input("Ingresa una letra: ").lower()

        if letra_usuario in letras_adivinadas:
            print("Ya has ingresado esa letra Inténtalo de nuevo.")
            continue

        letras_adivinadas.add(letra_usuario)

        if letra_usuario not in palabra:
            print("Letra incorrecta. Intentalo de nuevo.")
        else:
            palabra_oculta = mostrar_palabra(palabra, letras_adivinadas)
            print(palabra_oculta)

if __name__ == "__main__":
    palabras = generar_palabras()
    jugar_adivinanzas(palabras)
