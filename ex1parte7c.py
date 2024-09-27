import random
#c
vetor = []

for i in range(100):
   
    num = random.randint(1,100)
    if (num > 20):
        vetor.append(num)

print(vetor)
