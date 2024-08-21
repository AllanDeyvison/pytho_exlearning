# Definição das variáveis
num_corredores = 6
num_voltas = 10

# Leitura dos dados
corredores = []
tempos = []

for i in range(num_corredores):
    nome = input(f"Digite o nome do corredor {i+1}: ")
    corredores.append(nome)
    tempos_voltas = []
    for j in range(num_voltas):
        tempo = float(input(f"Digite o tempo da volta {j+1} do corredor {nome}: "))
        tempos_voltas.append(tempo)
    tempos.append(tempos_voltas)

# Melhor volta da prova
melhor_tempo = float('inf')
melhor_corredor = ""
melhor_volta = 0

for i in range(num_corredores):
    for j in range(num_voltas):
        if tempos[i][j] < melhor_tempo:
            melhor_tempo = tempos[i][j]
            melhor_corredor = corredores[i]
            melhor_volta = j + 1

print(f"\nMelhor volta da prova: {melhor_corredor} na volta {melhor_volta} com o tempo de {melhor_tempo} segundos.")

# Classificação final
tempos_totais = []
for i in range(num_corredores):
    tempo_total = sum(tempos[i])
    tempos_totais.append((tempo_total, corredores[i]))

tempos_totais.sort()

print("\nClassificação final:")
for i, (tempo_total, corredor) in enumerate(tempos_totais):
    print(f"{i+1}º lugar: {corredor} com tempo total de {tempo_total} segundos.")

# Volta com a média mais rápida
media_voltas = [0] * num_voltas

for j in range(num_voltas):
    soma_tempos = 0
    for i in range(num_corredores):
        soma_tempos += tempos[i][j]
    media_voltas[j] = soma_tempos / num_corredores

volta_mais_rapida = media_voltas.index(min(media_voltas)) + 1

print(f"\nVolta com a média mais rápida: Volta {volta_mais_rapida} com tempo médio de {min(media_voltas)} segundos.")
# Definição das variáveis
num_corredores = 6
num_voltas = 10

# Leitura dos dados
corredores = []
tempos = []

for i in range(num_corredores):
    nome = input(f"Digite o nome do corredor {i+1}: ")
    corredores.append(nome)
    tempos_voltas = []
    for j in range(num_voltas):
        tempo = float(input(f"Digite o tempo da volta {j+1} do corredor {nome}: "))
        tempos_voltas.append(tempo)
    tempos.append(tempos_voltas)

# Melhor volta da prova
melhor_tempo = float('inf')
melhor_corredor = ""
melhor_volta = 0

for i in range(num_corredores):
    for j in range(num_voltas):
        if tempos[i][j] < melhor_tempo:
            melhor_tempo = tempos[i][j]
            melhor_corredor = corredores[i]
            melhor_volta = j + 1

print(f"\nMelhor volta da prova: {melhor_corredor} na volta {melhor_volta} com o tempo de {melhor_tempo} segundos.")

# Classificação final
tempos_totais = []
for i in range(num_corredores):
    tempo_total = sum(tempos[i])
    tempos_totais.append((tempo_total, corredores[i]))

tempos_totais.sort()

print("\nClassificação final:")
for i, (tempo_total, corredor) in enumerate(tempos_totais):
    print(f"{i+1}º lugar: {corredor} com tempo total de {tempo_total} segundos.")

# Volta com a média mais rápida
media_voltas = [0] * num_voltas

for j in range(num_voltas):
    soma_tempos = 0
    for i in range(num_corredores):
        soma_tempos += tempos[i][j]
    media_voltas[j] = soma_tempos / num_corredores

volta_mais_rapida = media_voltas.index(min(media_voltas)) + 1

print(f"\nVolta com a média mais rápida: Volta {volta_mais_rapida} com tempo médio de {min(media_voltas)} segundos.")
