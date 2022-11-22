nome = input('Digite o seu nome: ').lower()
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
faltas = int(input('Digite o total de faltas: '))

total_aula = 20
min_presenca = total_aula * 0.7
min_media = 6
resultado = []

media = (nota1 + nota2) / 2
assiduidade = total_aula - faltas

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


print('Nome:',nome)
print('Média:',media)
print('Percentual de presença:',(assiduidade / total_aula) * 100)
print(resultado)
