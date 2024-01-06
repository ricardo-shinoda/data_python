
pergunta = 's'
fatura = []
total = 0
item = []
valid_preco = False

while pergunta == 's':
    produto = input('Qual o nome do produto? ')

    while valid_preco == False:
        preco = input('Qual o preço do produto? ')
        try:
            preco = float(preco)
            if preco <= 0:
                print('O preço não pode ser menor que zero')
            else:
                valid_preco = True
        except:
            print("Formato de preço inválido. Use apenas números e separe os centavos com '.'.")

    pergunta = input('Deseja comprar mais alguma coisa? S ou N? ').lower()
    fatura.append([produto,preco])
    valid_preco = False
    total += preco

for i in fatura:
    print(i[0], ':','R$',i[1])
print('O total da fatura é:','R$',total)