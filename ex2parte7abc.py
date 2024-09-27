# Criação do dicionário
dictionary = {}
for i in range(97, 123):
    dictionary[chr(i)] = i - 96

# Impressão do dicionário-a
print(dictionary)

# Impressão das letras cujo valor é múltiplo de 3-b
for letter, value in dictionary.items():
    if value % 3 == 0:
        print(letter)

# Eliminação dos elementos cujo valor é múltiplo de 5-c
to_delete = []
for letter, value in dictionary.items():
    if value % 5 == 0:
        to_delete.append(letter)
for letter in to_delete:
    del dictionary[letter]

print(dictionary)

# Acrescenta o elemento ("xx": 100) no final da lista-d
dictionary["xx"] = 100

print(dictionary)
