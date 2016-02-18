import random 

def jogo(max_=1000):
    numero = random.randint(0, max_)
    print("Escolhi um número entre 0 e {}, tente adivinhar:".format(max_))

    tentativas = 1
    while True:
        chute = input("Palpite: ")
        chute = int(chute)
        if chute == numero:
            print("Parabéns, você acertou em  {} tentativas".format(tentativas))
            break
        if chute < numero:
            print("Tente um número maior")
        else:
            print("Tente um número menor")
        tentativas += 1

def principal():
    while True:
        jogo(30)
        opcao = input("Quer jogar de novo?")
        if  opcao[0].lower() != "s":
            break
principal()