# DESAFIO 064
# ESTRUTURA WHILE

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS
# O PROGRAMA SÓ PODE PARAR QUANDO O USUÁRIO DIGITAR 999
# NO FIM, DEVE MOSTRAR QUNTOS NÚMEROS FORAM DIGITADOS
# E QUAL A SOMA DELES
# DESCONSIDERANDO O 999

'''
numero = 0
soma = -999
contador = -1
while numero != 999:
    numero = int(input('Digite um número: [999 para finalizar o programa]   '))
    contador += 1
    soma = soma + numero
print('Você digitou {} números.'.format(contador))
print('A soma dos números digitados é igual a {}.'.format(soma))
'''

# SEGUNDO O PROFESSOR ESSE MEU JEITO DE FAZER É MAIS OU MENOS CORRETO
# HEHEHEHE
# A FORMA CORRETA É COLOCANDO O COMANDO DO LADO DE FORA DO LAÇO WHILE
# PORQUE SE O FLAG FOR DIGITADO, ELE NÃO ENTRA NEM NA SOMA E NEM NO CONTADOR
# E COM ISSO EU NÃO PRECISO COLOCAR SOMA E CONTADOR NEGATIVOS
# A FORMA MAIS CORRETA É ASSIM:

contador = soma = 0
numero = int(input('Digite um número: [999 para parar]  '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número: [999 para parar]  '))
print('Você digitou {} números.'.format(contador))
print('A soma deles é {}.'.format(soma))

# SEGUNDO O PROFESSOR
# ESSA MANEIRA AINDA NÃO É A MAIS CORRETA DE SER FEITO
# E A VARIÁVEL SOMA E CONTADOR, POR ESTAREM NEGATIVADOS, PODEM GERAR PROBLEMAS
