# Funções
# function without argument

# def mensagem():
#     print('Seja bem-vindo!')

# print(mensagem())

# #Function with argument

# user = 'ricardo'
# def mensagem(nome):
#     print('Seja bem-vindo ' + nome.title()) #.title() para colocar primeira letra maiúscula

# mensagem('lucas')
# mensagem(user)

def imc(peso, altura):
    calculo = (peso / (altura * altura))
    return('Seu imc é: ',calculo)

if imc(80, 1.74) > 32:
    print('Obesidade')
else:
    print('Ainda não está obeso')

imc()

# if imc(70, 1.74) < 18:
#     print('Seu imc é: ',imc,'sua classificação é: abaixo do peso')
# elif imc(70, 1.74) >= 25 and imc(70, 1.74) < 30:
#     print('Seu imc é: ',imc,'sua classificação é: Sobrepeso')
# elif imc(70, 1.74) >= 18.5 and imc(70, 1.74) < 24.9:
#     print('Seu imc é: ',imc,'sua classificação é: normal')
# else:
#      print('Seu imc é: ',imc,'sua classificação é: Obesidade I')

# imc(70, 1.70)