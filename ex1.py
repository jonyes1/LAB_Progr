nota = float(input("Digite a nota do aluno (de 0 a 20): "))

if nota >= 9.5:
    if nota > 16:
        print("APROVADO (com distinção) ORAL")
    else:
        print("APROVADO")
else:
    print("REPROVADO")
