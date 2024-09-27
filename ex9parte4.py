import random

def jogo(n):
    # Número que o jogador A pensou:
    numero = random.randint(1, 100)
    
    for i in range(n):
        # Jogador B faz uma tentativa:
        palpite = int(input("Digite um número entre 1 e 100: "))
        
        # Verifica se o palpite é o número correto:
        if palpite == numero:
            print("Parabéns, acertaste!")
            return
        
        # Verifica se o palpite é maior ou menor que o número correto:
        if palpite > numero:
            print("O número é menor.")
        else:
            print("O número é maior.")
    
    # Se chegou aqui, o jogador B não acertou dentro do número de tentativas:
    print("As tentativas acabaram. O número correto era: ", numero)

# Teste:
jogo(2)
