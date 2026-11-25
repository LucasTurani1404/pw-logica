quantidade = 0
total = 0
preco = float(input("Digite o preço do produto: \n",
                    "(Digite 0 para encerra) \n",
                    "R$ "))

while preco != 0:
    total += preco
    quantidade += 1

    preco = float(input("Digite o preco do próximo produto: \n",
                        "(Digite 0 para encerrar) \n",
                        "R$ "))
    print(f"Total da Compra: R$ {total:.2f}")
    print(f"Quantidade de produtos: {quantidade}")