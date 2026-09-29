# Matriz pra sei lá oq
matriz = [
    [" ", " "],
    [" ", " "],
    [" ", " "]
]

# Usuário vai ter que preencher uma posição apenas com inteiros
for linha in range(3):
    for coluna in range(2):
        while True:
            try:
                valor = int(input(f"Digite um número inteiro para [{linha + 1}] [{coluna + 1}]: "))
                matriz[linha][coluna] = valor
                break
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números inteiros.")

# Agora o sistema vai exibir a matriz
print("\nMatriz Final:")
for i, linha in enumerate(matriz):
    print(f" {linha[0]} | {linha[1]} ")
    if i < 2:
        print("=======")

# Vai verificar qual o maior número apresentado até o momento
maior_numero = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior_numero:
            maior_numero = valor

print(f"\nO maior número digitado foi {maior_numero}")