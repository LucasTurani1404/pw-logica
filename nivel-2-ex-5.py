numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\n--- RESULTADO ---")
print("Todos os números:", numeros)
print("Números pares:", pares)
print("Quantidade de pares:", len(pares))
print("Números ímpares:", impares)
print("Quantidade de ímpares:", len(impares))