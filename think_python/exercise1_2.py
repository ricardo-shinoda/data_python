
# ? Quantos segundos há em 42 minutos e 42 segundos?
seconds = print((42*60) + 42)

# * response 2562

# ? Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

km_mil = 10 / 1.61

miles_km = print(km_mil)

# * 6.21

# ? Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

# Definindo a distância em quilômetros
distancia_km = 10

# Convertendo para milhas
distancia_milhas = distancia_km / 1.61

# Definindo o tempo em minutos e segundos
tempo_minutos = 42
tempo_segundos = 42

# Convertendo o tempo para minutos
tempo_total_minutos = tempo_minutos + tempo_segundos / 60

# Calculando o passo médio em minutos por milha
passo_medio_minutos_por_milha = tempo_total_minutos / distancia_milhas

# Convertendo para minutos e segundos
passo_medio_minutos = int(passo_medio_minutos_por_milha)
passo_medio_segundos = int(
    (passo_medio_minutos_por_milha - passo_medio_minutos) * 60)

# Calculando a velocidade média em milhas por hora
velocidade_media_milhas_por_hora = distancia_milhas / \
    (tempo_total_minutos / 60)

# Exibindo os resultados
print(f"Passo Médio: {passo_medio_minutos} minutos {
      passo_medio_segundos} segundos por milha")
print(f"Velocidade Média: {
      velocidade_media_milhas_por_hora:.2f} milhas por hora")
