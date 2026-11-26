opcao = 0
while opcao != 4:
    print("\n===== Menu de operações =====")
    print("1 - Mostrar mensagem de Boas-vindas!")
    print("2 - Mostrar a tabuada de um número")
    print("3 - Informar se um número é par ou ímpar")
    print("4 - Sair")
    opcao = int(input("Escolher uma opção: "))
    if opcao == 1:
            print("\nSeja bem-vindo ao programa!")
    elif opcao == 2:
          numero = int(input("Digite um número para ver a tabuada: "))
          for contador in range(1, 11):
            print(f"{numero} X {contador} = {numero * contador}")
    elif opcao == 3:
         numero = int(input("Digite um número: "))
if numero % 2 == 0:
            print(f"O número {numero} é PAR!")
else:
            print(f"O número {numero} é ÍMPAR!")
    elif opcao == 4:
print("\n Encerrando o programa... Até mais!")
else:
print("Opção Inválida!")