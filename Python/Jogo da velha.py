# Jogo da velha
# É válido ressaltar que são necessários dois jogadores pra esse jogo. Fiz uma outra versão usando IA, onde é se joga contra o computador, enfim, só um disclaimer
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"

for rodada in range(9):

    # Mostrar o tabuleiro
    print()
    print(tabuleiro[0][0], "|", tabuleiro[0][1], "|", tabuleiro[0][2])
    print("--+---+--")
    print(tabuleiro[1][0], "|", tabuleiro[1][1], "|", tabuleiro[1][2])
    print("--+---+--")
    print(tabuleiro[2][0], "|", tabuleiro[2][1], "|", tabuleiro[2][2])
    print()

    print("Jogador", jogador)

    linha = int(input("Digite a linha (1-3): "))
    coluna = int(input("Digite a coluna (1-3): "))

    linha = linha - 1
    coluna = coluna - 1

    # Verificar se a posição está ocupada
    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada!")
        continue

    # Colocar X ou O
    tabuleiro[linha][coluna] = jogador

    # Verificar linhas
    if (tabuleiro[0][0] == jogador and
        tabuleiro[0][1] == jogador and
        tabuleiro[0][2] == jogador) or \
       (tabuleiro[1][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[1][2] == jogador) or \
       (tabuleiro[2][0] == jogador and
        tabuleiro[2][1] == jogador and
        tabuleiro[2][2] == jogador):

        print("Jogador", jogador, "venceu!")
        break

    # Verificar colunas
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][0] == jogador and
        tabuleiro[2][0] == jogador) or \
       (tabuleiro[0][1] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][1] == jogador) or \
       (tabuleiro[0][2] == jogador and
        tabuleiro[1][2] == jogador and
        tabuleiro[2][2] == jogador):

        print("Jogador", jogador, "venceu!")
        break

    # Verificar diagonais
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador) or \
       (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):

        print("Jogador", jogador, "venceu!")
        break

    # Trocar jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

else:
    print("Empate!")
