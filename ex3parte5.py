#função que calcula a média
def calcularMedia(vetor):
    soma = 0
    for num in vetor:
        soma += num
    media = soma / len(vetor)
    return media

vetor = [1, 2, 3, 4, 5]
media = calcularMedia(vetor)
print(f"A média do vetor {vetor} é: {media}")
