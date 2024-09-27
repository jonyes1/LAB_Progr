menor = 99999999999

for i in range(10):
    numerop = int(input("Qual é o numero (positivo):"))
   
    if numerop < menor:

        menor = numerop

print("O menor número digitado é: ", menor)