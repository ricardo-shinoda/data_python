# Para imprimir cada elemento da lista

compras = ['arroz','feijao','macarrao','carne']

for i in compras:
    print(i)

# para inprimir cada letra
nome = 'ricardo'

for i in nome:
    print(i)


# Somatória com loop

vendas = [100,450,300,920,600]
total = 0

for i in vendas:
    total += i
print(total)

# total parcialmente adicionados

vendas = [100,450,300,920,600]
total = 0

for i in vendas:
    total += i
    print(total)



# For loop com dicionários - para trazer as chaves

cores = {'verde': 'green', 'red': 'vermelho'}

for i in cores:
    print(i)

    cores = {'verde': 'green', 'red': 'vermelho'}


# para imprimir os valores

for i in cores:
    print(cores[i])

# imprimindo os dois campos

for i in cores:
    print(i,':',cores[i])



# loop for aninhado

# imprimindo todos os objetos da lista
compras = [['arroz','feijao','macarrao'],['carne','frango'],['açúcar','chocolate']]

for i in compras:
    print(i)

# para imprimir a lista de todos os itens dentro da lista
for i in compras:
    for item in i:
        print(item)


# Range

for i in range(0,10):
    print(i)

# Contagem regressiva

for i in range(0,10):
    print(10-i)