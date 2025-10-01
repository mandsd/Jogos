import random

# Configuração: número de dígitos da senha e máximo de tentativas
DIGITOS = 4
MAX_TENTATIVAS = 10

# Gera um código secreto aleatório
def gerar_codigo():
    codigo = ''
    for i in range(DIGITOS):
        codigo += str(random.randint(0, 9))
    return codigo

# Verifica a tentativa em relação ao código secreto
def verificar_tentativa(codigo, tentativa):
    exatos = 0
    parciais = 0
    for i in range(DIGITOS):
        if codigo[i] == tentativa[i]:
            exatos += 1
        elif tentativa[i] in codigo:
            parciais += 1
    return (exatos, parciais)

# Loop principal do jogo
def jogar():
    print('SENHA')
    print('')
    print('Tente adivinhar o código de {} dígitos em {} tentativas ou menos.'.format(DIGITOS, MAX_TENTATIVAS))
    print('Dígitos vão de 0 a 9.')
    print('')
    
    codigo = gerar_codigo()
    tentativas = 0
    
    while tentativas < MAX_TENTATIVAS:
        tentativa = input('Tentativa {}: '.format(tentativas + 1))
        
        if len(tentativa) != DIGITOS:
            print('Tentativa inválida. Deve ter {} dígitos.'.format(DIGITOS))
            continue
        if not tentativa.isdigit():
            print('Tentativa inválida. Deve conter apenas dígitos.')
            continue
        
        tentativas += 1
        resultado = verificar_tentativa(codigo, tentativa)
        
        if resultado[0] == DIGITOS:
            print('Parabéns! Você acertou o código em {} tentativas.'.format(tentativas))
            return
        else:
            print('Resultado: {} no lugar certo, {} em outro lugar.'.format(resultado[0], resultado[1]))
            print('')
    
    print('Fim de jogo! Suas tentativas acabaram. O código secreto era {}.'.format(codigo))

# Inicia o jogo
jogar()
