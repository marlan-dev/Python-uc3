

palavra = "cachorro"
letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_erradas = []
def forca_jogo(palavra, letras_descobertas, tentativas, letras_erradas):
    while tentativas > 0:
        print(" ".join(letras_descobertas))
        print("Erros:", letras_erradas)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra.")
        

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        if "_" not in letras_descobertas:
            break
    else:
        print("Você perdeu! A palavra era:", palavra)

    if "_" not in letras_descobertas:
        print("Parabéns! Você acertou a palavra:", palavra)

forca_jogo(palavra, letras_descobertas, tentativas, letras_erradas)


