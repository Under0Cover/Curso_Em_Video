# DESAFIO 074
# TUPLAS

# CRIE UM PROGRAMA QUE VAI GERAR 05 NÚMEROS ALEATÓRIOS E COLOCAR NUMA TUPLA
# DEPOIS MOSTRE A LISTAGEM DESSES NÚMEROS
# E INDIQUE QUAL É O MAIOR E QUAL É O MENOR NÚMERO DESSA TUPLA

from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados são: {numeros}')

# PARA MOSTRAR O MAIRO VALOR E O MENOR VALOR O PYTHON TEM UMA FACILIDADE
# QUE PERMITE NÃO USAR TODA AQUELA ESTRUTURA DE IF JÁ MOSTRADA NO CURSO
# UTILIZAMOS O MAX(VARIAVEL) E MIN(VARIAVEL)
# FICANDO ASSIM:
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')