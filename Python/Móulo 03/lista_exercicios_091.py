# DESAFIO 091
# ESTRUTURA DICIONÁRIOS

# CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO
# GUARDE OS RESULTADOS EM UM DICIONÁRIO
# NO FINAL COLOQUE ESSE DICIONÁRIO EM ORDEM
# SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO

from random import randint
from time import sleep
from operator import itemgetter

resultado = {'Jogador 01': randint(1, 6), 'Jogador 02': randint(1, 6),
             'Jogador 03': randint(1, 6), 'Jogador 04': randint(1, 6)}
ranking = []
print('Valores sorteados:')
sleep(2)
for keys, values in resultado.items():
    print(f'O {keys} tirou {values} no dado!')
    sleep(1)
ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print('-=' * 40)
print('CLASSFICAÇÃO:')
sleep(2)
for indice, value in enumerate(ranking):
    print(f'O {indice + 1}º lugar ficou com o {value[0]} com {value[1]} tirado nos dados!')
    sleep(1)
