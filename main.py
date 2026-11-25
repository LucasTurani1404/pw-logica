numero = int(input("Digite um número inteiro positivo: "))
pares = 0
impares = 0

for contador in range(1, numero + 1)

    if contador % 2 == 0:
        pares += 1
    else:
        impares += 1
print (f"Quantidade de numeros pares {pares}")
print (f"Quantidade de numeros impares {impares}")
