contador = 1

while contador <= 5:
  
  print("Olá mundo!")
  
  contador = contador + 1

while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0:
        break
    print("Idade inválida! Tente novamente.")

print("Idade registrada!")

while True:
   
   numero = int(input("Digite um número inteiro positivo: "))

for contador in range(1, numero + 1):
    print(contador)

numero = int(input("Digite um número inteiro: "))

for contador in range( 1, 11):
    resultado = numero * contador
    print(f"{numero}x{contador}={resultado}")

exemplo_nivel 
1

aluno1 = "pedro"
aluno2 = "joão"
aluno3 = "Tubas"
aluno4 = "Lorenzo"

alunos = ["Pedro", "joão", "Tubas", "Lorenzo"]

print(alunos)

ou

alunos = ["Pedro", "joão", "Tubas", "Lorenzo"]

print(alunos[0])
print(alunos[1])
print(alunos[2])
print(alunos[3])
print(alunos[4])

outro

alunos = ["Pedro", "joão", "Tubas", "Lorenzo"]

print(alunos)

alunos.append("Erick")

print(alunos)


quantidade = len(alunos)
print(f"Temos {quantidade} alunos cadastrados.")

for aluno in alunos:
    print(f"Olá, {aluno}!")