# DESAFIO 045
# ESTRUTURAS IF-ELIF-ELSE

# JOKENPO

from random import randint
from time import sleep
print(' -=-=- JOKENPO -=-=-')
opcoes = ('Papel', 'Tesoura', 'Pedra')
computador = randint(0, 2)
print('Escolha uma das opções para jogar com o computador')
print('0- Papel')
print('1- Tesoura')
print('2- Pedra')
jogador = int(input('Escolha a sua opção: '))
sleep(1)
print('JO')
sleep(1)
print('  KEN')
sleep(1)
print('     PO')
sleep(2)
print('-=-' * 40)
sleep(1)
print('Você escolheu {}'.format(opcoes[jogador]))
sleep(2)
print('Computador jogou {}'.format(opcoes[computador]))
sleep(1)
print('-=-' * 40)
if computador == 0: # 0 - Papel
    if jogador == 0: # 0 - Papel
        print('EMPATOU O JOGO!')
    elif jogador == 1: # 1 - Tesoura
        print('Jogador VENCEU!')
    else: # 2 - Pedra
        print('Computador VENCEU!')
elif computador == 1: # 1 - Tesoura
    if jogador == 0: # 0 - Papel
        print('Computador VENCEU!')
    elif jogador ==1: # 1 - Tesoura
        print('EMPATOU O JOGO!')
    else: # 2 - Pedra
        print('Jogador VENCEU!')
else: # 2 - Pedra
    if jogador == 0: # 0 - Papel
        print('Jogador VENCEU!')
    elif jogador == 1: # 1 - Tesoura
        print('Computador VENCEU!')
    else: # 2 - Pedra
        print('EMPATOU O JOGO!')