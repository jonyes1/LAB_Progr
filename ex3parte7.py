pessoas = []
total_pessoas = 0
soma_idade = 0
mulheres = []
acima_media = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['sexo'] = input('Digite o sexo da pessoa (M/F): ')
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    
    pessoas.append(pessoa)
    total_pessoas += 1
    soma_idade += pessoa['idade']
    
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa)
        
    continuar = input('Deseja continuar? (S/N) ')
    if continuar.upper() == 'N':
        break
        
media_idade = soma_idade / total_pessoas

for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa)
        
print(f'Foram registadas {total_pessoas} pessoas.')
print(f'A média de idade é de {media_idade:.2f} anos.')
print('Mulheres: ')
for mulher in mulheres:
    print(mulher['nome'])
print('Pessoas com idade acima da média: ')
for pessoa in acima_media:
    print(f'{pessoa["nome"]}, {pessoa["idade"]} anos')

