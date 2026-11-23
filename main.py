while True:
    print("___ Calculadora ___\n"
    "1- Somar \n"
    "2- Subtrair \n"
    "3- Multiplicar \n"
    "4- Sair \n")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 4:
      print("Encerrando Calculadora...")
      break
    if opcao == 1:
      print("você escolheu Somar")
      break
    elif opcao == 2:
      print("você escolheu Subtrair")
      break
    elif opcao == 3:
      print("você escolheu Multiplicar")
      break
    else:
      print("Opção inválida!")