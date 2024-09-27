import math

cateto1 = float(input("Qual é o valor do primeiro cateto: "))
cateto2 = float(input("Qual é o valod do segundo cateto: "))

hipotenusa = math.sqrt((cateto1 * cateto1) + (cateto2 * cateto2))

print("O valor da hipotenusa é: ", hipotenusa)