import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif jogador == "pedra" and computador == "tesoura":
    print("Você ganhou! Pedra quebra tesoura")
elif jogador == "papel" and computador == "pedra":
    print("Você ganhou! Papel embrulha pedra")
elif jogador == "tesoura" and computador == "papel":
    print("Você ganhou! Tesoura corta papel")
else:
    print("Você perdeu!")