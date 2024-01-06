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
    print(sorted(jogo)) # para ordenar uma lista

megasena()

# Função Choice (para escolher aleatóriamente alguim item da lista - fazer um sorteio)

alunos = ['Luísa','Lucas', 'Paula', 'Ricardo']
print(random.choice(alunos))

# Pegar uma amostra de uma lista

print(random.sample(alunos, 2))