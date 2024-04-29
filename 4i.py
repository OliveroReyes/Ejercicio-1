import random
import time

def generar_arreglo(longitud):
    return [random.randint(0, 9) for _ in range(longitud)]

def mostrar_arreglo(arreglo, tiempo):
    print("Memoriza el arreglo:")
    print(arreglo)
    time.sleep(tiempo)
    print("Tiempo terminado. Ahora ocultaré los números.")

def jugar_memoria(arreglo):
    print("¡Bienvenido al juego de memoria!")
    mostrar_arreglo(arreglo, 3)
    for num in arreglo:
        intento = int(input("Ingresa el próximo número del arreglo: "))
        if intento != num:
            print("¡Incorrecto! Has perdido.")
            return False
    print("¡Felicidades! Has recordado todos los números correctamente. ¡Has ganado!")
    return True

if __name__ == "__main__":
    longitud_arreglo = 5
    arreglo = generar_arreglo(longitud_arreglo)
    jugar_memoria(arreglo)
