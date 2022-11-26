import imc_function as f #nome do arquivo que eu estou importando, tem .nome para usar a função abaixo

print('Vamos validar o seu IMC?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o seu sexo (M ou F) ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo diferente de M ou F.')
    else:
        valid_sexo = True
        print('\n') # para pular uma linha

valid_peso = False
while valid_peso == False:
    peso = input('Digite o seu peso: ')
    try:
        peso = float(peso)
        if peso < 0:
            print('Valor deve ser maior que 0.')
        else:
            valid_peso = True
            print('\n') # para pular uma linha
    except:
        print('Use apenas números e separe os decimais com ponto.')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a sua altura: ')
    try:
        altura = float(altura)
        if altura < 0:
            print('Valor deve ser maior que 0.')
        else:
            valid_altura = True
            print('\n') # para pular uma linha
    except:
        print('Use apenas números e separe os decimais com ponto.')

v_imc = str(f.imc(peso, altura))
c_imc = f.class_imc(sexo, peso, altura)
print('O seu imc é: ',v_imc[0:5])
print('A sua classificação é: ', c_imc)
