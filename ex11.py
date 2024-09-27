número1 = int(input("Introduz o primeiro número: "))
número2 = int(input("Introduz o segundo número: "))

soma = número1 + número2
print("O valor da soma é: ", soma)

if soma > 20: 
    soma = soma + 8
    print("O valor da soma é final(segundo restrições do ex): ", soma)

elif soma <= 20:
    soma = soma - 5
    print("O valor da soma é final(segundo restrições do ex): ", soma)