def leer_arreglo():
    elementos = input("Ingresa los elementos del arreglo separados por espacios: ")
    arreglo = list(map(int, elementos.split()))
    return arreglo

def contar_pares(arreglo):
    pares = sum(1 for num in arreglo if num % 2 == 0)
    return pares

arreglo = leer_arreglo()
resultado = contar_pares(arreglo)
print("El número de elementos pares en el arreglo es:", resultado)