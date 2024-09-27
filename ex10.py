import math 

a = int(input("Digite um número para o valor de a: "))
b = int(input("Digite um número para o valor de b: "))
c = int(input("Digite um número para o valor de c: "))

delta = b**2 - 4*a*c

if delta > 0:
   raizdelta = math.sqrt(delta)
   x1 = (-b + raizdelta)/(2*a)
   x2 = (-b - raizdelta)/(2*a)
   print("O valor das duas raizes reais é: ", x1, x2)
elif delta == 0:
    x3 = -b/(2*a)
    print("O valor da raiz real é: ", x3)
else: # delta menor que 0
    print("A equação não possui raízes reais")