# Inicializa a lista de médias dos alunos
medias = []

# Laço para solicitar as notas de cada aluno
for i in range(10):
    notas = []
    print(f"Informe as notas do aluno {i+1}: ")
    for j in range(4):
        notas.append(float(input(f"Nota {j+1}: ")))
    media = sum(notas) / len(notas)
    medias.append(media)

# Conta o número de alunos com média maior ou igual a 7.0
num_alunos_aprovados = 0
for media in medias:
    if media >= 7:
        num_alunos_aprovados += 1

# Imprime o resultado na tela
print(f"O número de alunos com média maior ou igual a 7.0 é: {num_alunos_aprovados}")
