alunostotais = 60
alunosfaltaram = int(input("Quantos alunos faltaram ao exame: "))

alunospmedia = alunostotais - alunosfaltaram

media = 0
for i in range (alunospmedia):

    nota = float(input("Qual e a nota do aluno :"))

    media = nota / alunospmedia
    print("A média do aluno é:", media)