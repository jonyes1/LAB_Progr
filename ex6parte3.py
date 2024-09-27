import random
total = 0

djchernobil = 0
for djchernobil in range(1, 21, 1): #soma do chernobyl

    number = random.randint(1,15)

    
    total = total + number

media = total / 20

if media > 8:

    media = 10


print("A a média é:", media)