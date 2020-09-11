# DESAFIO 028
# TESTE DE ADIVINHAÇÃO

# CRIE UM PROGRAMA QUE VAI ESCOLHER UM NÚMERO DE 0 A 5
# O USUÁRIO TENTARÁ ADVINHAR O NÚMERO ESCOLHIDO


import random
from time import sleep
# FUNCIONALIDADE COMO O SYSTEM('PAUSE')

numero_pc = random.randint(0, 5)
print('O Computador vai escolher um número de 0 a 5')
sleep(2)
print('Quero saber se você consegue acertar qual número é esse...')
sleep(2)
print('Pensando....')
sleep(3)
print('Pronto, já pensei...')
numero_usuario = int(input('Qual número eu pensei? '))
if numero_usuario == numero_pc:
    print('Parabéns!!! Você acertou o número...')
else:
    print('Eu pensei no número {} e você digitou o número {}'.format(numero_pc, numero_usuario))
