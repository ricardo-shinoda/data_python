color = {'vermelho': 'red', 'verde': 'green',
         'azul': 'blue', 'amarelo': 'yellow'}
# cor = input('Digite uma cor: ').lower()  # transformar tudo em letra minúscula
# traducao = color.get(cor, 'Esta cor não consta no meu dicionário')
# print(traducao)

# The type
print(type(color))

# Lentgh of the dictionary
print(len(color))

# Delete
del color['vermelho']

# To know if there is a key in the dictionary
print('verde' in color)
