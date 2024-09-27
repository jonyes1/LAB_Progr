frase = input("Digite uma frase: ")
letraescolhida = input("Digite uma letra: ")

contador = 0

for letra in frase:
    if letra in letraescolhida:
        contador += 1
    
print("Existem", contador, "letras", letraescolhida, "na frase escolhida\n")    

posicoes = [] #lista vazia
for i in range(len(frase)):
     if frase[i] == letra:
        posicoes.append(i)

print("A letra aparece nas posições:", posicoes)