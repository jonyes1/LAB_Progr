nota = float(input("Qual foi a nota do aluno (0-20): "))

if nota < 5:
    print("Péssimo")
elif nota >= 5 and nota < 8:
    print("Mau")
elif nota >= 8 and nota < 10:
    print("Insuficiente")
elif nota >= 10 and nota < 12:
    print("Suficiente")
elif nota >= 12 and nota < 16:
    print("Bom")
elif nota >= 16 and nota < 20:
    print("Excelente")