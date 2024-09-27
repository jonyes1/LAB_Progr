a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    a, b = b, a

contador = 0

for i in range(a, b+1):
    if i % 2 == 0:
        contador = contador + 1

print("Existem {} números pares entre {} e {}".format(contador, a, b))