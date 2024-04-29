numero = int(input("Ingresa un número entero positivo: "))
suma_impares = 0
for i in range(1, numero + 1):
    if i % 2 != 0:
        suma_impares += i

print("La suma de los números impares desde 1 hasta", numero, "es:", suma_impares)