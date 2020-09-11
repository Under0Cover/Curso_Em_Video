# DESAFIO 016
# UM PROGRAMA QUE RECEBE NÚMEROS REAIS E IMPRIMA APENAS O NÚMERO INTEIRO

from math import trunc
numero = float(input('Digite um número real: '))
num_inteiro = trunc(numero)
print('O número inteiro de {}, é {}!'.format(numero, num_inteiro))

''' OUTRA FORMA DE FAZER SEM IMPORTAR A BIBLIOTECA DE MATEMÁTICA

NUM = FLOAT(INPUT('DIGITE UM VALOR: '))
PRINT('O VALOR DIGITADO FOI {} E A SUA PORÇÃO INEIRA É {}'.FORMAT(NUM, INT(NUM)))'''