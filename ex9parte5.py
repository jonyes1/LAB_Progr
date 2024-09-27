idade = []
altura = []

for i in range(5):
    alturas = float(input("Qual é a altura da pessoa: "))
    altura.append(alturas)
    idades = int(input("Qual é a idade da pessoa: "))
    idade.append(idades)

print(altura[::-1])
print(idade[::-1])
