import random

# print(random.randint(0,10000))

def megasena(): # jogo aleatório mega-sena
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1,60)
        if num in jogo:
            continue
        else:
            jogo.append(num)
    print(jogo)

megasena()