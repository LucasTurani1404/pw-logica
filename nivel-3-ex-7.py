opcao = 0
while opcao != 5:
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
        alunos = ["ana vitória", "Maria Laura", "Tubas Barbosa", "Lorenzo Barbosa", "Henrique Sicsu", "Arthur Abadi", "Willian Petry", "Ana Clara"]
        for contador in range(8):
    
                AnaVi = "Aluno 1: Ana Vitória"
                Maria = "Aluno 2: Maria Laura"
                Tubas = "Aluno 3: Tubas Barbosa"
                Lorenzo = "Aluno 4: Lorenzo Barbosa"
                Henrique = "Aluno 5: Henrique Sicsu"
                Arthur = "Aluno 6: Arthur Abadi"
                Willian = "Aluno 7: Willian Petry"
                AnaCla = "Aluno 8: Ana Clara"
                print (AnaVi)
                print (Maria)
                print (Tubas)
                print (Lorenzo)
                print (Henrique)
                print (Arthur)
                print (Willian)
                print (AnaCla)
       
       
                       
                
    elif opcao == 3:
        print(alunos)
    aluno = input("Escolha um para Remover: ")
    alunos.remove(aluno)
    print(alunos)

    if opcao == 4:
        quantidade = len(alunos)
    print(f"Temos {quantidade} Alunos cadastrados")
    
if opcao == 5:
    print("Fechando...")
else:
    print("Essa opção inválida")    
    
        
