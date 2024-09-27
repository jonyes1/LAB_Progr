perguntas = ['Telefonou à vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia dinheiro à vítima?', 'Já trabalhou com a vítima?']

respostas = []
for pergunta in perguntas:
    resposta = input(pergunta + "(sim ou não): ")
    if resposta == 'sim':
        respostas.append(True)
    else:
        respostas.append(False)

num_respostas_positivas = sum(respostas)
if num_respostas_positivas == 2:
    print('Suspeita')
elif 3 <= num_respostas_positivas <= 4:
    print('Cúmplice')
elif num_respostas_positivas == 5:
    print('Assassino')
else:
    print('Inocente')