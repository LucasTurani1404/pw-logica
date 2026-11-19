print("=== CONVERSOR UNIVERSAL ===")
print("1 - Temperatura (Celsius para Fahrenheit)")
print("2 - Distância (Km para Milhas)")
print("3 - Dinheiro (Reais para Dólar)")
print("4 - Peso (Kg para Libras)")


escolha = int(input("Escolha uma opção: "))

if escolha == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")

elif escolha == 2:
    km = float(input("Digite a distância em Km: "))
    milhas = km * 0.621371
    print(f"{km} km = {milhas:.2f} milhas")

elif escolha == 3:
     reais = float(input("Digite o valor em Reais (R$): "))
     cotacao = float(input("Digite a cotação do dólar hoje: "))
     dolares = reais / cotacao
     print(f"R$ {reais:.2f} = US$ {dolares:.2f}")

elif escolha == 4:
    kg = float(input("Digite o peso em Kg: "))
    libras = kg * 2.20462
    print(f"{kg} kg = {libras:.2f} libras")

else:
    print("Opção inválida!")