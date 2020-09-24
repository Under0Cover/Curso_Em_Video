# DESAFIO 073
# TUPLAS

# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS
# DO CAMPEONATO BRASILEIRO NA ORDEM DE COLOCAÇÃO
# DEPOIS DÊ 04 RETORNOS
# A) APENAS OS 5 PRIMEIROS
# B) OS 4 ÚLTIMOS COLOCADOS
# C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
# D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE

# OBS 1: O TIME DA CHAPECOENSE NÃO ESTÁ NA SÉRIE A
# TROQUEI PELO TIME DO FORTALEZA
# OBS 2: A DATA DA CONSULTA É 22:18 DO DIA 23/09/20
# NO MOMENTO DO EXERCÍCIO HAVIA UM JOGO EM ANDAMENTO
# SPORT 1 X 0 CORINTHIANS
# A TABELA ESTAVA ATÉ ENTÃO, ATUALIZADA COM ESSE RESULTADO

escalacao_times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras',
                   'Vasco', 'Flamengo', 'Sport', 'Santos', 'Fortaleza',
                   'Fluminense', 'Ceará', 'Grêmio', 'Corinthians',
                   'Atlético-GO', 'Atlético-PR', 'Coritiba', 'Bragantino',
                   'Botafogo', 'Bahia', 'Goiás')
for pos, times in enumerate(escalacao_times):
    print(f'{pos + 1}ª Posição - {times}')
print('-=-' * 20)
print(f'Os 5 primeiros times são {escalacao_times[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos times são {escalacao_times[-4:]}')
print('-=-' * 20)
print(f'Os times da primeira divisão em ordem alfabética {sorted(escalacao_times)}')
print('-=-' * 20)
print(f'O time do Fortaleza está na {escalacao_times.index("Fortaleza") + 1}ª posição')

