#função que calcula a média
def Imprimirmaiorvalor(vetor):

    maior = 0
    for num in vetor:
       if num > maior:
         maior = num

    return maior

vetor = [1.1, 2.5, 3.6, 4, 5, 19.5]
maior = Imprimirmaiorvalor(vetor)
print(f"O maior número do vetor {vetor} é: {maior}")
