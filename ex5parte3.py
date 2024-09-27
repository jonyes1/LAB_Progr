maior = -float('inf')
menor = float('inf')

while True:
    num = int(input("Digite um número positivo (ou -1 para sair): "))
    
    if num == -1:
        break
    
    if num < 0:
        print("Número inválido. Digite um número positivo.")
        continue #faz parar aqui o código e volta ao início do loop
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num
        
print(f"O maior número digitado foi {maior} e o menor foi {menor}.")
#ou
#print("O maior número digitado foi {} e o menor foi {}.".format(maior, menor))


