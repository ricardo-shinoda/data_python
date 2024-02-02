import time

# Obtém o tempo atual em segundos desde a época
tempo_atual = time.time()

# Converte o tempo em horas, minutos e segundos
horas = int(tempo_atual // 3600)
minutos = int((tempo_atual % 3600) // 60)
segundos = int(tempo_atual % 60)

# Converte o tempo em dias desde a época
dias_desde_epoca = int(tempo_atual // (3600 * 24))

# Imprime os resultados
print(f'Tempo atual: {horas} horas, {minutos} minutos, {segundos} segundos')
print(f'Dias desde a época: {dias_desde_epoca} dias')
