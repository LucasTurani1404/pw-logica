nome = input("Seu nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento
ano_100 = ano_nascimento + 100

print(f"{nome}, você tem (ou vai fazer) {idade} anos em {ano_atual})")
print(f"Você vai completar 100 anos em {ano_100}")