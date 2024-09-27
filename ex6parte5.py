vetorN = []
vetorpar = []
vetorimpar = []

for i in range (1,21):
    elementos = int(input(f"Insere os elemento {i} para o vetor:"))
    vetorN.append(elementos)

    if elementos % 2 == 0:
        vetorpar.append(elementos) 
    else:
        vetorimpar.append(elementos)


print("O vetor par compõe os seguintes elementos:",vetorpar)        
print("O vetor impar compõe os seguintes elementos:",vetorimpar)     