lado1 = float(input("Introduz o valor do primeiro lado : "))
lado2 = float(input("Introduz o valor do segundo lado: "))
hipotenusa = float(input("Introduz o valor da hipotenusa: "))


if lado1 == lado2 or lado1 == hipotenusa or lado2 == hipotenusa:
    print("O triângulo é isósceles")
    
elif lado1 == lado2 == hipotenusa: 
    print("O triângulo é equilátero")
else:
    print("O triângulo é escaleno")