def leer_arreglo():
    elementos = input("Ingresa los elementos del arreglo separados por espacios: ")
    arreglo = list(map(int, elementos.split()))
    return arreglo

def media_arreglo(arreglo):
    media = sum(arreglo) / len(arreglo)
    return media

arreglo = leer_arreglo()
resultado = media_arreglo(arreglo)
print("La media de los elementos del arreglo es:", resultado)