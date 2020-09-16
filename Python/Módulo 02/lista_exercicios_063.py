# DESAFIO 063
# ESTUTURA WHILE

# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO
# E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS
# DE UMA SEQUÊNCIA FIBONACCI

print('-=-' * 20)
print('Calculando a Sequência de Fibonacci')
print('-=-' * 20)
numero = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1

print('{} -> {}'.format(termo1, termo2), end=' ')
contador = 3
while contador <= numero:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end=' ')
    #AGORA EU TENHO QUE FAZER O TERMO1 E O TERMO2 ASSUMIREM NOVOS VALORES PARA CONTINUAR A SEQUÊNCIA
    termo1 = termo2
    # O TERMO1 OCUPA O ESPAÇO DO TERMO2
    termo2 = termo3
    # O TERMO2 OCUPA O ESPAÇO DO TERMO3
    # ASSIM A SOMA DO TERMO3 LÁ EM CIMA, PASSA A 'CAMINHAR'
    contador +=1
    # CONTADOR + 1 PARA ENCONTRAR O TOTAL DO NÚMERO REQUISITADO FORA DO WHILE
print(' ')
print('Sequência finalizada')
print('\nFIM DO PROGRAMA')
