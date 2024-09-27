import random

gelado = 0
maior = 0

while gelado == 0:
    number = random.randint(1,1000)
    print(number)

    if number > maior:
        maior = number

    if number % 7 == 0:  
        gelado = 1

print("\nO número maior é :", number)
