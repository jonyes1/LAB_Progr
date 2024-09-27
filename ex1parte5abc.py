# Parte A
lista_A = []

# Lendo valores para a lista A de dimensão 10
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor para a lista A: "))
    lista_A.append(valor)

# Invertendo a ordem dos elementos da lista A
lista_A = lista_A[::-1]

# Parte B
# Imprimindo a nova lista A
print("A nova lista A, com a ordem dos elementos invertida, é:")
print(lista_A)

# Parte C
# Alterando o programa para que a lista A tenha dimensão 100
nova_lista_A = []

# Ler valores para a nova lista A de dimensão 100
for i in range(100):
    valor = int(input(f"Digite o {i+1}º valor para a nova lista A: "))
    nova_lista_A.append(valor)

# Invertendo a ordem dos elementos da nova lista A
nova_lista_B = nova_lista_A[::-1]

# Imprimindo a nova lista A com dimensão 100
print("A nova lista A com dimensão 100, com a ordem dos elementos invertida, é:")
print(nova_lista_B)
