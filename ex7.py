número1 = int(input("Introduz o primeiro número: "))
número2 = int(input("Introduz o segundo número: "))

if número1 > número2:
    print("O menor número é:", número2)
elif número1 < número2:
    print("O menor número é:", número1)
elif número1 == número2:
    print("Iguais")