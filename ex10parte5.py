A = [] #cria um vetor vazio
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)

soma_quadrados = 0 #inicializa a soma com zero
for num in A: #itera pela lista A
    soma_quadrados += num**2 #calcula a soma dos quadrados dos elementos em A

print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)
