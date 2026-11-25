import random
numero_secreto = random.randint(1,20)
tentativas = 0
palpite = int(input(
    "Tente adivinhar um numero entre 1 e 20:"))
while palpite != numero_secreto:
    tentativas += 1
    if palpite < numero_secreto:
        print("numero_secreto é maior!")
    else:
        print("O numero secreto é menor!")
        palpite = int(input("Tente novamente: "))
tentativas += 1
print("Parabéns! Você acertou!")
print(f"O número secreto era: {numero_secreto}")
print(f"Você utilizou {tentativas} tentativas.")