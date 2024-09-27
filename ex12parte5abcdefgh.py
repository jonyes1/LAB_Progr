notas = []
valor = 0

# Leitura das notas
while valor != -1:
    valor = int(input("Digite uma nota (-1 para finalizar): "))
    if valor != -1:
        notas.append(valor)

# a. Quantidade de valores lidos
print("Quantidade de valores lidos:", len(notas))

# b. Valores na ordem em que foram inseridos
print("Valores na ordem em que foram inseridos:", notas)

# c. Valores na ordem inversa à que foram inseridos
print("Valores na ordem inversa à que foram inseridos:", notas[::-1])

# d. Soma dos valores
soma = sum(notas)
print("Soma dos valores:", soma)

# e. Média dos valores
media = soma / len(notas)
print("Média dos valores:", media)

# f. Quantidade de valores acima da média
acima_da_media = sum(1 for nota in notas if nota > media)
print("Quantidade de valores acima da média:", acima_da_media)

# g. Quantidade de valores abaixo de 10 (negativas)
abaixo_de_10 = sum(1 for nota in notas if nota < 10)
print("Quantidade de valores abaixo de 10:", abaixo_de_10)

# h. Quantidade de valores acima de 10 (positivas)
acima_de_10 = sum(2 for nota in notas if nota > 10)
print("Quantidade de valores acima de 10:", acima_de_10)      