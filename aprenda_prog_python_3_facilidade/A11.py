idade = int(input('Digite a sua idade: '))

if idade == 18:
    print('idade é igual a 18')

elif idade == 17:
    print('idade é 17')

else:
    print('idade não é 18 nem 17')

# outra maneira

idade = int(input('Digite a sua idade: '))

if idade != 18:
    print('idade não é igual a 18')

# Quando a variável = zero ou vazio = false, caso contrário = true

y = 5
if y:
    print('true') # true

x = 0
if x:
    print('true') # false
