print("=== CONVERSOR DE ARMAZENAMENTO ===")

bytes = float(input("Digite a quantidade de bytes: "))
kb = float(input("Digite a quantidade de kb: "))
mb = float(input("Digite a quantidade de mb: "))

resultado_kb = bytes / 1024
resultado_mb = kb /1024
resultado_gb = mb / 1024

print("\n=== RESULTADOS ===")

print(f"{bytes} Bytes = {resultado_kb:.2f} KB")
print(f"{kb} KB = {resultado_mb:.2f} MB")
print(f"{MB} = {resultado_gb:.2f} GB")