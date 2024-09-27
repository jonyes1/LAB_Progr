import math

numero = float(input("Digite um número: "))

if numero >= 0:
    raizquadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raizquadrada)
else:
    quadrado = numero ** 2
    print("O quadrado de", numero, "é" ,quadrado)

# ** elevado a x