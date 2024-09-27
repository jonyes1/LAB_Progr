frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

contador = 0

for letra in frase: #vai ler todas as letras da frase
    if letra in vogais: #vai comparar essas letras com as vogais,se for vogal o contador incrementa para 1
        contador += 1

print("A frase digitada contém", contador, "vogais.")