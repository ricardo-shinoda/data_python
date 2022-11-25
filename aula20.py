sexo = input('Digite o seu sexo "m" ou "h": ')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
resultado = []

print('Seu sexo é: ',sexo)
print('Seu peso é: ', peso)
print('Sua altura é: ',altura)

def imc(peso, altura):
    calculo = (peso / (altura * altura))
    return(calculo)

if sexo == 'm':
    if imc(peso, altura) < 19.1:
        print('Abaixo do peso')
    elif imc(peso, altura) > 19.1 and imc(peso, altura) <= 25.8:
        print('no peso normal')
    elif imc(peso, altura) > 25.8 and imc(peso, altura) <= 27.3:
        print('marginalmente acima do peso')
    elif imc(peso, altura) > 27.3 and imc(peso, altura) <= 32.3:
        print('acima do peso ideal')
    else:
        print('obesa')
elif sexo == 'h':
    if imc(peso, altura) < 20.7:
        print('Abaixo do peso')
    elif imc(peso, altura) > 20.7 and imc(peso, altura) <= 26.4:
        print('no peso normal')
    elif imc(peso, altura) > 26.4 and imc(peso, altura) <= 27.8:
        print('marginalmente acima do peso')
    elif imc(peso, altura) > 27.8 and imc(peso, altura) <= 31.1:
        print('acima do peso ideal')
    else:
        print('Obeso')