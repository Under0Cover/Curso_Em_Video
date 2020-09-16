# DESAFIO 058
# ESTRUTURA WHILE

# REFAÇA O DESAFIO 028
# NESSA ATUALIZAÇÃO O JOGADOR VAI TENTAR ADVINHAR ATÉ ACERTAR
# MOSTRANDO NO FINAL QUANTAS TENTATIVAS NECESSÁRIAS PARA VENCER O COMPUTADOR

# MINHA RESOLUÇÃO
'''
from random import randint
from time import sleep
numero_pc = randint(0, 10)
print('O computador esconlheu um número de 0 a 10')
print('Você vai tentar advinhar esse número!')
numero_pess = -1
palpites = 0
while numero_pc != numero_pess:
    numero_pess = int(input('Digite um número: '))
    if numero_pess != numero_pc:
        sleep(2)
        print('Número errado!')
        print('Tente novamente!')
        print('-=-' * 20)
        palpites += 1
sleep(2)
print('FINALMENTE VOCÊ ACERTOU!!!')
print('O número escolhido pelo Computador foi o {}'.format(numero_pc))
print('Você precisou de {} palpites para acertar'.format(palpites))
'''

# RESOLUÇÃO DO PROFESSOR COM TOQUES MEUS
from random import randint
# randint PARA SORTEAR UM NÚMERO INTEIRO
computador = randint(0, 10)
# AQUI DIZEMOS QUAIS OS NÚMEROS ELE PODE SORTEAR
print('Oi, eu sou seu computador!')
print('Acabei de pensar em um número entre 0 e 10')
print('Você é capaz de adivinhar qual é esse número?')
# JÁ QUE É UM JOGO, NÉ?!
acertou = False
# VARIÁVEL DE CONTROLE DE ACERTO
palpites = 0
# VARIÁVEL PRA CONTAR A QUANTIDADE DE PALPITES
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    # CADA TENTAVIVA CONTABILIZA UM PALPITE
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior')
        else:
            print('Tente um número menor')
            # ESSA ERA A PARTE QUE EU NÃO TINHA ADICIONADO NO MEU
# AQUI INICIOU A VARIÁVEL acertou COMO FALSA
# E VAI COMPARAR AS RESPOSTAS
# WHILE ENQUANTO acertou FOR FALSO
print('Acertou, Mizeravi!')
print('Só precisou de {} tentativas'.format(palpites))
