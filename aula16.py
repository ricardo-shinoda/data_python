
pergunta = 's'
fatura = []
total = 0

while pergunta == 's':
    produto = input('Qual o nome do produto?')
    preco = float(input('Qual o preço do produto?'))
    pergunta = input('Deseja comprar mais alguma coisa? S ou N?').lower()
    fatura.append(preco)

for i in fatura:
    total += i

print(total)