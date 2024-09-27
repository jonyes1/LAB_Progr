import time

# função para temporizador de contagem decrescente
def countdown(t):
    while t > 0:
        print(t)
        time.sleep(0.1)
        t -= 1
    print("Tempo esgotado!")

# função para jogo de terminal que conta o tempo em contagem decrescente
def jogo_tempo_limite(tempo):
    print("Iniciando o jogo...")
    print(f"Você tem {tempo} segundos para vencer!")
    countdown(tempo)
    print("Fim de jogo!")

# exemplo de uso da função de jogo de terminal
jogo_tempo_limite(10)  # jogar com tempo limite de 10 segundos
