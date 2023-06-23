def jogar_forca():

    import random
    import lista_palavras # lista de 20 palavras possíveis para acertar
    from unidecode import unidecode

    palavra = random.choice(lista_palavras.palavras)
    palavra_sem_acento = unidecode(palavra)
    silhueta_palavra = []
    letras_digitadas = []
    enforcou = False
    acertou = False
    tentativas = 10
    i = 0
    
    print("\n### Jogo da Forca ###")
    print(f"A palavra tem {len(palavra)} letras")

    # cria a silhueta da palavra
    for letra in palavra:
        if letra == " ":
            silhueta_palavra.append(" ")
        else:
            silhueta_palavra.append("_")

    print("\n", "".join(silhueta_palavra), "\n")

    # roda o jogo até ganhar ou enforcar
    while(not enforcou and not acertou):

        # é mostrado sempre o histórico de letras digitadas
        # Exemplo = Histórico: a, g, j, e
        print("Histórico:", ",".join(letras_digitadas))

        # é mostrado sempre a qtd atual de tentativas 
        print(f"Tentativas: {tentativas}")    

        # O usuário digita uma letra ou chute de cada vez
        saida_user = (str(input("Digite: "))).lower()

        if saida_user in letras_digitadas:
        
            print("\nLetra já digitada!\n")
        
        else:    

            letras_digitadas.append(saida_user)
             
            # verifica se a letra está na palavra
            for letra in palavra_sem_acento:
                if letra == saida_user:
                    silhueta_palavra[i] = palavra[i]    
                i += 1  
            i = 0

            silhueta_na_tela = "".join(silhueta_palavra)

            # se a letra não estiver na palavra
            if saida_user not in palavra_sem_acento:
                tentativas -= 1

            # mostra ao user a silhueta da palavra
            print("\n", "".join(silhueta_palavra), "\n")

        # se o user digitou todas as letras corretas antes da forca
        if silhueta_na_tela == palavra:
            print("Você acertou!")
            acertou = True    

        # quando as tentativas acabarem
        if tentativas == 0:
            print("FORCA! A palavra não foi atingida completamente")
            print(f"A palavra era: {palavra}")
            enforcou = True

        # se o user tentar um chute (ou seja quando ele digitar mais de uma letra)
        if len(saida_user) > 1:
            if saida_user == palavra:
                print("Belo chute! Você acertou!")
                acertou = True
            else: 
                print("Chute errado. Continue tentando!")    
                tentativas -= 1

    # verifica se o user quer ou não jogar de novo
    print("\nDeseja jogar novamente? (s/n)")

    while True: 
        resposta_jogardenovo = str(input("Digite: "))       
        if resposta_jogardenovo == "s":
            jogar_forca()
        elif resposta_jogardenovo == "n":                
            print("\nFim!")
            break
        else:    
            print("\nEscolha inválida")


# roda o jogo
if (__name__ == "__main__"):
    jogar_forca()