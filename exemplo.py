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