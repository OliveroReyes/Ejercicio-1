producto = 1
print("Ingresa números enteros positivos. Ingresa un número negativo para terminar.")
while True:
    numero = int(input("Ingresa un número: "))
    if numero < 0:
        break
    else:
        producto *= numero
print("El producto de los números enteros positivos ingresados es:", producto)