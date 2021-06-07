import forca
import advinhacao

def escolhe_jogos():
    print("***********************************")
    print("****Bem vindo, Escolha seu jogo****")
    print("***********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Escolha o jogo: "))
    if(jogo == 1):
        print("Jogondo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogos()