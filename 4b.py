def leer_arreglo():
    elementos = input("Ingresa los elementos del arreglo separados por espacios: ")
    arreglo = list(map(int, elementos.split()))
    return arreglo

def maximo_arreglo(arreglo):
    maximo = max(arreglo)
    return maximo

arreglo = leer_arreglo()
resultado = maximo_arreglo(arreglo)
print("El elemento máximo del arreglo es:", resultado)