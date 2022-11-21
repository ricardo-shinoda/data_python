# print("meu primeiro programa em python")
# print('O resultado de 2+ 3 é', 2+3)
# print("fim do programa")

# # variáveis

# minha_idade = 42
# print('Eu tenho', minha_idade, 'anos')

# taxaUSD = 3.20
# qtd = 100
# print('O valor total convertido é de:',taxaUSD * qtd)

# nome = "Lucas"
# nome_mae = "Maroubo"
# nome_pai = "Shinoda"
# nome_completo = nome + ' ' + nome_mae + ' ' + nome_pai
# print(nome_completo)

# print(len(nome)) # para saber o comprimento de uma variável
# print(nome[0]) # para saber um determinado valor do index
# print(nome[-1]) # mesmo que o de cima, mas de trás pra frente
# print(nome[0:2]) # para fatiar o valor - o primeiro não conta "Lu"
# print(nome[-2:]) # as
# print(nome[:3]) # Luc

# # Exercício trazendo as iniciais do nome

# inicial = nome[0] + nome_mae[0] + nome_pai[0]
# print(inicial)

# # Exercício montando o e-mail com nome pessoal e da empresa

# nome = 'ricardo'
# sobrenome = 'shinoda'
# empresa = "boticario"
# email = nome + '.' + sobrenome + '@' + empresa + '.com'
# print(email)

# # funções matemáticas

# import math

# raiz_quadrada = math.sqrt(16)
# print(raiz_quadrada) # 4.0

# # Exercicio

# # num1 = int(input('Type a number: '))
# # num2 = int(input('Type another number: '))
# # print('O resultado da soma de',num1, 'e', num2, 'é igual a', num1 + num2)

# # exercício 2 média poderada

# nota1 = float(input('Qual é a primeira nota?'))
# nota2 = float(input('Qual é a segunda nota?'))
# print('A média ponderada é', (nota1 + nota2) / 2)

# # Aula 6 criando tupla
# # tuplas são imutáveis, não podem sofrer alterações, as listas podem

# meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
# print(meses)
# print(type(meses))

# alunos = ['maria', 'pedro', 'helena']
# print(type(alunos))


# alunos[1] = 'ricardo' # para atualizar um valor na lista
# print(alunos)

# alunos.append('lucas') # para adicionar um valor na lista
# print(alunos)

# alunos.insert(1, 'paula') # para adicionar um elemento em um determinado index da lista

# alunos.sort() # para ordenar os valores da lista
# print(alunos)

# alunos.pop(1) # para retirar um item de um determinado index da lista

# alunos.remove('paula') # para remover um determinado valor da lista
# print(alunos)

# alunos2 = ['joaquina', 'godofredo', 'alfredo']
# total = alunos + alunos2
# print(total)

# # exercício mês de nascimento

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

data = input('Digite a sua data de nascimento no formato: DD-MM-AAAA ')
print('Sua data de aniversário é ',data)
mes = data[3:5]
mes_final = meses[int(mes)-1]
print('Você nasceu no mês de',mes_final)

