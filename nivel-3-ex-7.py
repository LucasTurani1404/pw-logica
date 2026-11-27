opcao = 0
while opcao != 4:
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar Aluno")
    print("2 - Listar Aluno")
    print("3 - Remover aluno")
    print("4 - Quantidade de alunos")
    print("5- Sair")
    opcao = int(input("Escolher uma opção: "))
    if opcao == 1:
            Cadastrar = input("Cadastrar um Aluno: ")
            alunos.append(Cadastrar)
            print(alunos)
    elif opcao == 2:
        alunos = ["Ana Vitória", "Maria Laura", "Tubas Barbosa", "Lorenzo Barbosa", "Henrique Sicsu", "Arthur Abadi", "Willian Petry", "Ana Clara"]
