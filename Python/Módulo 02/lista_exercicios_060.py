# DESAFIO 060
# ESTRUTURA WHILE

# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO
# E FAÇA O SEU FATORIAL
# OBS: FATORIAL É A MULTIPLICAÇÃO DOS NÚMEROS ATÉ O 2
# EX: 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2

# USANDO A BIBLIOTECA MATH
'''
from math import factorial
numero = int(input('Digite um número para ser fatorado: '))
resultado = factorial(numero)
print('O número {} fatorado é {}'.format(numero, resultado))
'''

# FAZENDO NA BASE DA DEMONSTRAÇÃO
# EM ALGUMAS LINGUAGENS NÃO HÁ ESSA FUNÇÃO FATORIAL NAS BIBLIOTECAS (?)

numero = int(input('Digite um número para ser fatorado: '))
contador = numero
fatorial = 1
print('Calculando {}! = '.format(numero))
while contador > 0:
    print('{}'.format(contador), end=' ')
    # COLOCAR AS MULTIPLICAÇÕES EM LINHA
    print(' x ' if contador > 1 else ' = ', end=' ')
    # PRINT PARA MOSTRAR O SINAL DE MULTIPLICAÇÃO OU IGUAL
    # OTIMIZANDO A CONTA
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
