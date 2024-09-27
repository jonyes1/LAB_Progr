soma_idades = 0
qtd_regular = 0
qtd_bom = 0
qtd_excelente = 0

for i in range(1,21):
    idade = int(input("Digite a idade do espectador: "))
    opiniao = int(input("Digite a opinião do espectador (1-regular, 2-bom, 3-excelente): "))
    
    if opiniao == 3:
        qtd_excelente += 1
        soma_idades += idade
    elif opiniao == 1:
        qtd_regular += 1
    elif opiniao == 2:
        qtd_bom += 1

if qtd_excelente > 0:

    media_idades_excelente = soma_idades / qtd_excelente 

else: 
    media_idades_excelente = 0

percentagembom = (qtd_bom / 20) * 100

print("Média das idades das pessoas que responderam 'excelente':", media_idades_excelente)
print("Quantidade de pessoas que responderam 'regular':", qtd_regular)
print("Percentagem de pessoas que responderam 'bom':", percentagembom, "%")