horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

segundosh = 3600 * horas
segundosm = 60 * minutos

nst = segundos + segundosh + segundosm

print("O número de segundos totais é: ", nst)