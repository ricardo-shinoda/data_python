import time

# print(time.localtime())

# hora = time.localtime().tm_hour
# print('The hour is: ',hora) # para imprimir a hora

# tempo = time.localtime()
# minute = tempo.tm_min
# print('The minute is: ',minute)

# relogio = time.process_time()
# relogio2 = time.perf_counter()
# print(relogio) 
# print(relogio2)

def count_time():
    inicio = time.perf_counter()
    input('Escreva o seu nome: ')
    final = time.perf_counter()
    tempo = round(final - inicio,2)
    print('Você levou: ' + str(tempo) + ' segundos para escrever o seu nome')

count_time()