def leer_arreglo():
    elementos = input("Ingresa los elementos del arreglo separados por espacios: ")
    arreglo = list(map(int, elementos.split()))
    return arreglo

def suma_arreglo(arreglo):
    suma = sum(arreglo)
    return suma

arreglo = leer_arreglo()
resultado = suma_arreglo(arreglo)
print("La suma de los elementos del arreglo es:", resultado)
