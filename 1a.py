def determinar_signo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

numero = int(input("Ingresa un número entero: "))

signo = determinar_signo(numero)

print(f"El número ingresado es {signo}.")