print("Insira a nota do Aluno:")
nota1 = float (input("\t(0-20): "))
nota2 = float (input("\t(0-20): "))

média = (nota1 + nota2)/2
print("A média do aluno é:", média)

if média >= 9.5:
    print("Aprovado")
else:
    print("Reprovado")