def leer_arreglo():
    elementos = input("Ingresa los elementos del arreglo separados por espacios: ")
    arreglo = list(map(int, elementos.split()))
    return arreglo

def minimo_arreglo(arreglo):
    minimo = min(arreglo)
    return minimo

arreglo = leer_arreglo()
resultado =minimo_arreglo(arreglo)
print("El elemento minimo del arreglo es:", resultado)