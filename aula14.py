# x = 0
# pessoas = []

# while x < 4:
#    nome = input('Qual o seu nome? ')
#    pessoas.append(nome)
#    x += 1

# print(pessoas)



# Loop até um determinado item entrar na lista:

x = 0
pessoas = []

while 'joao' not in pessoas:
    nome = input('Qual o seu nome? ')
    pessoas.append(nome)

print(pessoas)

x = 0
pessoas = []

while x < 4:
    nome = input('Qual o seu nome? ')
    if nome == 'joao':
        continue
    pessoas.append(nome)

print(pessoas)



