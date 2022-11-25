sexo = 'm'
valid_peso = False
valid_altura = False

def imc(peso, altura):
    calculo = (peso / (altura * altura))
    return(calculo)

while sexo == 'm':
    while valid_peso == False and valid_altura == False:
        sexo = input('Digite o seu sexo "m" ou "h": ')
        peso = input('Digite o seu peso: ')
        altura = input('Digite a sua altura: ')
        try:
            peso = float(peso)
            altura = float(altura)
            if peso <= 0:
                print('O peso não pode ser menor que zero')
            elif altura <= 0:
                print('A altura não pode ser menor que zero')
            else:
                valid_peso = True
                valid_altura = True
        except:
            print("Formato de peso ou altura inválido. Use apenas números e separe os gramas por ponto.")
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
while sexo == 'h':
    while valid_peso == False and valid_altura == False:
        sexo = input('Digite o seu sexo "m" ou "h": ')
        peso = input('Digite o seu peso: ')
        altura = input('Digite a sua altura: ')
        try:
            peso = float(peso)
            altura = float(altura)
            if peso <= 0:
                print('O peso não pode ser menor que zero')
            elif altura <= 0:
                print('A altura não pode ser menor que zero')
            else:
                valid_peso = True
                valid_altura = True
        except:
            print("Formato de peso ou altura inválido. Use apenas números e separe os gramas por ponto.")
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