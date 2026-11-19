num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

operacao = input("Escolha a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado:.2f}")

if operacao == "-":
    resultado = num1 - num2
    print(f"resultado: {resultado:.2f}")

    if operacao == "*":
        resultado = num1 * num2
        print(f"resultado: {resultado:.2f}")

    elif operacao == "/":
if num2 != 0:
    resultado = num1 / num2
    print(f"resultado: {resultado:.2f}")
else:
    print("Erro! Não pode dividir por zero!")
else:
print("Operação inválida!")