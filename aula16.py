produto = input('Qual o nome do produto?')
preco = input('Qual o preço do produto?')
pergunta = input('Deseja comprar mais alguma coisa? S ou N?').lower()

fatura = 0

while pergunta == 's':
    for i in produto:
        produto += i
        for x in preco:
            preco += x
print(produto)
print(preco)
