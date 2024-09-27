import random
#d
vetor = []

for i in range(99):
    
    num = random.randint(1,100)
    vetor.append(num)
    
vetor.insert(100,100)
print(vetor)


#e
print(len(vetor))

