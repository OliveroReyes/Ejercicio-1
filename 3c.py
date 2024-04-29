suma_numeros = 0
print("Ingresa números enteros positivos. Ingresa un número negativo para terminar.")
while True:
    numero = int(input("Ingresa un número: "))
    if numero < 0:
        break
    else:
        suma_numeros += numero
print("La suma de los números enteros positivos ingresados es:", suma_numeros)