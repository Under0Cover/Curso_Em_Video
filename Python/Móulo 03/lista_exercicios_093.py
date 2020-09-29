# DESAFIO 093
# ESTRUTURA DICIONÁRIO

# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL
# O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU
# DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA
# NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO
# INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
total_partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for contador in range(0, total_partidas):
    partidas.append(int(input(f'Quantos gols na partida {contador + 1}? ')))
jogador['Gols'] = partidas[:]
jogador['Total_Gols'] = sum(partidas)
print('-=' * 40)
print(jogador)
print('-=' * 40)
for chaves, indice in jogador.items():
    print(f'O campo {chaves} tem o valor {indice}!')
print('-=' * 40)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas e tem {jogador["Total_Gols"]} pelo clube!')
for indice, valores in enumerate(jogador['Gols']):
    print(f'        -> Na partida {indice + 1}, fez {valores} gols!')