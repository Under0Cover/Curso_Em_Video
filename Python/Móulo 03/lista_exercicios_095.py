# DESAFIO 095
# ESTRUTURA DICIONÁRIO

# APRIMORE O DESAFIO 093
# PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES
# INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR

plantel = list()
jogador = dict()
partidas = list()
while True:
    # CADASTRO DO JOGADOR
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    total_partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for contador in range(0, total_partidas):
        partidas.append(int(input(f'Quantos gols na partida {contador + 1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total_Gols'] = sum(partidas)
    plantel.append((jogador.copy()))
    # ADICONAR NOVOS JOGADORES?
    while True:
        resposta = str(input('Deseja cadastrar outro jogador? [S/N]: ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERROR! Por favor, digite S ou N!')
    if resposta == 'N':
        break
# CABEÇALHO
print('-=' * 40)
print(' Cod ', end='')
for indice in jogador.keys():
    print(f' {indice:<13}', end='')
print()
print('-=' * 40)
# TABELA DO PLANTEL
for indice, valores in enumerate(plantel):
    print(f' {indice:<5}', end='')
    for dados in valores.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-=' * 40)
# DETALHAMENTO DOS JOGADORES NAS PARTIDAS
while True:
    detalhamento = int(input('Detalhamento do jogador: '))
    if detalhamento == 999:
        break
    elif detalhamento >= len(plantel):
        print(f'ERROR! Não existe jogador com o código {detalhamento}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {plantel[detalhamento]["Nome"]}:')
        for indice, gols in enumerate(plantel[detalhamento]["Gols"]):
            print(f'    -> No jogo {indice + 1} fez {gols} gols.')
    print('-=' * 40)
print('Volte Sempre!')