color = {'vermelho': 'red', 'verde': 'green', 'azul': 'blue', 'amarelo': 'yellow'}
cor = input('Digite uma cor: ').lower() # transformar tudo em letra minúscula
traducao = color.get(cor, 'Esta cor não consta no meu dicionário')
print(traducao)
