# nome = input('Digite o seu nome: ').lower()
# nota1 = float(input('Digite a nota da primeira prova: '))
# nota2 = float(input('Digite a nota da segunda prova: '))
# faltas = int(input('Digite o total de faltas: '))

# total_aula = 20
# min_presenca = total_aula * 0.7
# min_media = 6
# resultado = []

# media = (nota1 + nota2) / 2
# assiduidade = total_aula - faltas

# if assiduidade >= min_presenca:
#     if media >= 6:
#         resultado = 'Aprovado'
#     elif media < 6:
#         resultado = 'Reprovado por media'
# elif assiduidade < min_presenca:
#     if media >= 6:
#         resultado = 'Reprovado por falta'
#     elif media < 6:
#         resultado = 'Reprovado por falta e por media'
# else:
#     print('Dados informados são inválidos')


# print('Nome:',nome)
# print('Média:',media)
# print('Percentual de presença:',str((assiduidade / total_aula) * 100)+' %')
# print(resultado)


name = input('Type the student name: ').lower()
result1 = float(input('Type first test result: '))
result2 = float(input('Type second test result: '))
missing_class = int(input('Type total missing class: '))

total_classes = 20
min_atendance = 0.7
final_result = []

media_prova = (result1 + result2) / 2
presenca = (missing_class / total_classes) * 100


if presenca >= min_atendance:
    if media_prova >= 6:
        final_result = ('Aluno aprovado')
    elif media_prova < 6:
        final_result = ('Reprovado por nota')
elif presenca < min_atendance:
    if media_prova < 6:
        final_result = ('Reprovado por nota e falta')
    elif media_prova > 6:
        final_result = ('Reprovado por falta apenas')
else:
    final_result = ('Dados incorredos, tente novamente')


print('The student name is: ', name)
print('The avegare exam result is: ', media_prova)
print('Attendance percentage is: ', presenca, '%')
print('The Result is: ', final_result)
