import random
def jogar():
    print("****************************************")
    print("****Bem vindo ao jogo de Adivinhação****")
    print("****************************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Esolha o nivel de dificuldade")
    print("(1) Fácil (2) Médio (3)Dificil")

    nivel = int(input("Escolha nivel: "))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas =5

    for rodada in range(1, total_tentativas + 1):

        print("Tentativa {} de {} ".format(rodada, total_tentativas)) 
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute= int(chute_str)
        if(chute < 1 or chute > 100):
            print("Número invalido, precisa ser um numero entre 1 e 100")
            continue
        print("Você digitou ", chute)

        acertou = chute == numero_secreto 
        maior = chute > numero_secreto 
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o numero secreto")
            elif(menor):
                print("Você errou! Seu chute foi menor que o numero secreto")   
            pontos_perdidos = abs(numero_secreto - chute) * 5
            pontos -= pontos_perdidos   

    print("Fim do jogo\nO número era {}".format(numero_secreto))

if(__name__ == "__main__"):
    print("entro")
    jogar()