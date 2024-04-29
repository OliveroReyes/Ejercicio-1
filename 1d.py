letra = input("Ingresa una letra del alfabeto: ").lower()  


if letra.isalpha() and len(letra) == 1:
    if letra in 'aeiou':
        print(f"{letra} es una vocal.")
    else:
        print(f"{letra} es una consonante.")
else:
    print("Por favor, ingresa solo una letra del alfabeto.")