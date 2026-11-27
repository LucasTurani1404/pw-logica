notas = []
soma = 0

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
    soma += nota  # variável acumuladora

maior = notas[0]
menor = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

media = soma / len(notas)

# 4. MOSTRAR TUDO
print("\n--- RESULTADO ---")
print("Todas as notas:", notas)
print("Soma:", soma)
print("Média:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)