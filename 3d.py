import random

corredor1 = 0
corredor2 = 0
tiempo = 0

while corredor1 < 100 and corredor2 < 100:
    corredor1 += random.randint(1, 5)
    corredor2 += random.randint(1, 5)
    tiempo += 1

if corredor1 >= 100 and corredor2 >= 100:
    print("¡Es un empate!")
elif corredor1 >= 100:

    print("El corredor 1 ganó en", tiempo, "segundos")
else:
    print("El corredor 2 ganó en", tiempo, "segundos")

