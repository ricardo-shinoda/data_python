nome = input('Digite o seu nome: ').lower()

valid_note = False
while valid_note == False:
    nota1 = input('Digite a nota da primeira prova: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('Valor deve ser entre 0 e 10')
        else:
            valid_note = True
    except:
        print('Use apenas números e separe os decimais com ponto')

valid_note = False
while valid_note == False:
    nota2 = input('Digite a nota da segunda prova: ')
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('Valor deve ser entre 0 e 10')
        else:
            valid_note = True
    except:
        print('Use apenas números e separe os decimais com ponto')


valid_falta = False
while valid_falta == False:
    falta = input('Digite o número de falta(s): ')
    try:
        falta = float(falta)
        if falta < 0 or falta > 20:
            print('Qtd de falta deve ser entre 0 e 20')
        else:
            valid_falta = True
    except:
        print('Use apenas números e separe os decimais com ponto')

total_aula = 20
min_presenca = total_aula * 0.7
min_media = 6
resultado = []

media = (nota1 + nota2) / 2
assiduidade = total_aula - falta

if assiduidade >= min_presenca:
    if media >= 6:
        resultado = 'Aprovado'
    elif media < 6:
        resultado = 'Reprovado por media'
    elif assiduidade < min_presenca:
        if media >= 6:
            resultado = 'Reprovado por falta'
        elif media < 6:
            resultado = 'Reprovado por falta e por media'
        else:
            print('Dados informados são inválidos')
else:
    resultado = 'Reprovado por faltas'


print('Nome:',nome)
print('Média:',media)
print('Percentual de presença:',str((assiduidade / total_aula) * 100)+' %')
print(resultado)
