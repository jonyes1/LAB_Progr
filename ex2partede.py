# Criação do dicionário
dictionary = {}
for i in range(97, 123):
    dictionary[chr(i)] = i - 96

# Acrescenta o elemento ("xx": 100) no final da lista-d
dictionary["xx"] = 100

print(dictionary)

# Tamanho do dicionario-e
print(len(dictionary))