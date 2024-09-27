número1 = int(input("Introduz o primeiro número: "))
número2 = int(input("Introduz o segundo número: "))
número3 = int(input("Introduz o terceiro número: "))

if número1 > número2 and número1 > número3:
    print("O maior número é: ", número1)

elif número1 < número2 and número2 > número3:
     print("O maior número é: ", número2)

elif número3 > número1 and número3 > número2:
    print("O maior número é: ", número3)