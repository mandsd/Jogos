tab = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]  

def tabuleiro(tabu):  
    for i in range(len(tabu)):
        if i % 3 == 0:
            print()
            print('------------------------')
        else:    
            print()
        for j in range(len(tabu)):
            if j % 3 == 0 or  j == 9:
                print('|', end='')
            print(tabu[i][j],'', end='')
    print()
    print('------------------------')

tabuleiro(tab)

def options(fil, col):
    opcoes = [1,2,3,4,5,6,7,8,9]
    for fileira in range(9):
        valor = tab[fileira][col] 
        if valor == 0:
            continue
        if valor in opcoes:
            opcoes.remove(int(valor))   
    for coluna in range(9):
        valor = tab[fil][coluna] 
        if valor == 0:
            continue
        if valor in opcoes:
            opcoes.remove(int(valor))

    x = [int(fil/3), int(col/3)]
    
    for fileira in range(x[0] * 3, x[0] * 3 + 3):
         for coluna in range(x[1] * 3, x[1] * 3 + 3):
            valor = tab[fileira][coluna] 
            if valor == 0:
                continue
            if valor in opcoes:
                opcoes.remove(int(valor))
    return opcoes

def resolucao():
    for fileira in range(len(tab)):
        for coluna in range(len(tab[fileira])):
            if tab[fileira][coluna] == 0:
                opcoes = options(fileira,coluna)
                for n in opcoes:
                    tab[fileira][coluna] = n
                    if not resolucao():
                        tab[fileira][coluna] = 0
                return 0
    tabuleiro(tab)

resolucao()
