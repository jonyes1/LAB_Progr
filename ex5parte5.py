vetor = ['w', 'b', 'a', 'd']
soma = 0
vogais = ['a', 'e', 'i', 'o', 'u']
for letra in vetor:
    if letra in vogais:
        soma += 1
        for vogal in vogais:
            if letra == vogal:
                print(f"A letra '{vogal}' foi encontrada no vetor")


print(f"O vetor tem {soma} vogal/ais")
