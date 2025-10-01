# Se quiser, você pode mudar a palavra secreta!
palavra_secreta = "filmes"
letras_digitadas = []
erros = 0
letras_erradas = []

def desenhar(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if(erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("ERRO! Apenas uma letra, tente novamente!")
        continue

    letras_digitadas.append(letra)
    palavra_ate_agora = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            palavra_ate_agora += letra_secreta
        else:
            palavra_ate_agora += ' _ '

    if palavra_ate_agora == palavra_secreta:
        print("Parabéns, você ganhou :)")
        break
    else:
        print("Palavra secreta até agora: ", palavra_ate_agora)

    if letra not in palavra_secreta:
        if letra in letras_erradas:
            print("Essa letra já foi digitada, tente outra!")
        if letra not in letras_erradas:
            erros += 1
            desenhar(erros)
            letras_erradas.append(letra)
            print("Letras que não estão na palavra: ", str(letras_erradas).strip('[]'))
        print("")

    if erros >= 7:
        print("Você perdeu :(")
        print("A palavra era: ", palavra_secreta)
        break
