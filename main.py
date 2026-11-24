numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Erro, tem que ser positivo!")
else:
    soma = 0
    conta = ""

    for i in range(1, numero + 1):
        soma += i
        
        if i == numero:
            conta += str(i) 
        else:
            conta += str(i) + " + "

    print(f"{conta} = {soma}")