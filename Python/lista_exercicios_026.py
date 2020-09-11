# DESAFIO 026
# CRIE UM PROGRAMA QUE LEIA UM FRASE PELO TECLADO E MOSTRE:

frase = str(input('Digite uma frase: ')).strip().upper()

# A) QUANTAS VEZES APARECE A LETRA A
print('A letra "A" aparece {} vezes na frase!'.format(frase.count('A')))

# B) EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))

# C) EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))
