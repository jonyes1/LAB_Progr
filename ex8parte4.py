def menor_numero_moedas_notas(valor):
    notas = [50, 20, 10, 5, 2, 1] # Valores das notas e moedas em ordem decrescente
    num_notas = [] # Lista vazia para contar o número de notas e moedas
    
    for nota in notas:
        qtd_notas = valor // nota
        valor = valor - (qtd_notas * nota)  
        num_notas.append(qtd_notas)
    
    return num_notas


valor = int(input("Qual é o valor:"))
num_notas = menor_numero_moedas_notas(valor)
print(num_notas) # [1, 1, 1, 1, 0, 2] -> uma nota de 50, uma de 10, uma de 5, uma de 2, e duas de 1 euro