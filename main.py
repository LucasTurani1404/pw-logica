senha_correta = "1234"
tentativas = 3

while tentativas > 3:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    
    print("Senha errada!")
    tentativas += 3
else:
    print("Conta bloqueada!")