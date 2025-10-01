def resolver_sudoku(tabuleiro):
    # Encontra a próxima célula vazia
    linha, coluna = encontrar_celula_vazia(tabuleiro)

    # Se não houver células vazias, o Sudoku está resolvido
    if linha is None:
        return True

    # Tenta cada número de 1 a 9 na célula vazia
    for num in range(1, 10):
        if é_valido(tabuleiro, linha, coluna, num):
            # Coloca o número na célula vazia
            tabuleiro[linha][coluna] = num

            # Resolve recursivamente o resto do tabuleiro
            if resolver_sudoku(tabuleiro):
                return True

            # Se a tentativa recursiva falhou, volta atrás e tenta o próximo número
            tabuleiro[linha][coluna] = 0

    # Se nenhum número pode ser colocado, o Sudoku não tem solução
    return False


def encontrar_celula_vazia(tabuleiro):
    # Procura a próxima célula vazia no tabuleiro
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna
    return None, None


def é_valido(tabuleiro, linha, coluna, num):
    # Verifica se o número pode ser colocado na célula sem violar as regras do Sudoku

    # Verifica a linha
    if num in tabuleiro[linha]:
        return False

    # Verifica a coluna
    if num in [tabuleiro[i][coluna] for i in range(9)]:
        return False

    # Verifica o quadrado 3x3
    linha_caixa = (linha // 3) * 3
    coluna_caixa = (coluna // 3) * 3
    if num in [tabuleiro[i][j] for i in range(linha_caixa, linha_caixa + 3)
                              for j in range(coluna_caixa, coluna_caixa + 3)]:
        return False

    return True


# Exemplo de tabuleiro
tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Resolve o Sudoku
if resolver_sudoku(tabuleiro):
    # Imprime a solução
    for linha in tabuleiro:
        print(linha)
else:
    print("O Sudoku não tem solução.")
