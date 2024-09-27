# cria uma lista vazia para armazenar os nomes
nomes = []

# loop para aceitar os nomes de 20 pessoas
for i in range(20):
    nome = input("Digite o nome da pessoa: ".format(i+1)) # i+1 para começar no 1
    nomes.append(nome)

# exibe os nomes na tela
print("\nNomes digitados:")
for nome in nomes:
    print(nome)
