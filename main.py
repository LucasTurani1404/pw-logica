a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

#etapa 1
if a < b + c and b < a + c and c < a + b:

    print("Forma um triangulo!")

    #etapa 2
    if a == b and b == c:
        print("Triangulo Equilátero")

    elif a == b or a == c or b == c:
        print("Triangulo isóceles!")

    else:
        print("Triangulo Escaleno!")
else:
    print("Não forma um triangulo!")
