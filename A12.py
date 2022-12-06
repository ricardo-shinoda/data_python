idade = int(input('Digite a sua idade: '))
sexo = input('Digite o seu sexo: ').lower()
cidade = input('Digite a cidade: ').lower()

# if idade < 18 and sexo == 'm':
#     print('homem menor de idade')

# elif idade >= 18 and sexo == 'm':
#     print('homem maior de idade')

# elif idade < 18 and sexo == 'f':
#     print('mulher menor de idade')

# elif idade >= 18 and sexo == 'f':
#     print('mulher maior de idade')

# else:
#     print('erro na entrada de dados')

# outra maneira

# if sexo == 'm':
#     if idade < 18:
#         print('homem menor de idade')
#     elif idade >= 18:
#         print('homem maior de idade')
# elif sexo == 'f':
#     if idade < 18:
#         print('mulher menor de idade')
#     elif idade >= 18:
#         print('mulher maior de idade')
# else:
#     print('erro na entrada de dados')

# usando o OR

if cidade == 'rio' or cidade == 'sao paulo':
    print
    
    if sexo == 'm':
        if idade < 18:
            print('homem menor de idade, da região sudeste')
        elif idade >= 18:
            print('homem maior de idade, da região sudeste')
    elif sexo == 'f':
        if idade < 18:
            print('mulher menor de idade, da região sudeste')
        elif idade >= 18:
            print('mulher maior de idade, da região sudeste')
    else:
        print('erro na entrada de dados')
else:
    print('teste apenas para rio ou sao paulo')