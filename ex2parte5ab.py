# leitura das listas A e B
listaA = []
N = int(input("Digite o tamanho da lista A: "))
for i in range(N):
    elem = int(input("Digite o elemento {}: ".format(i+1)))
    listaA.append(elem)

listaB = []
M = int(input("Digite o tamanho da lista B: "))
for i in range(M):
    elem = int(input(f"Digite o elemento {i+1}: "))
    listaB.append(elem)

# união das listas A e B
listaC = listaA + listaB

# impressão das listas
print("Lista A: ", listaA)
print("Lista B: ", listaB)
print("Lista C (união de A e B): ", listaC)
