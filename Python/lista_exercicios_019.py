# DESAFIO 019
# SORTEANDO UM ITEM DA LISTA

from random import choice
aluno1 = input('Digite o nome do primeiro aluno a ser sorteado: ')
aluno2 = input('Digite o nome do segundo aluno a ser sorteado: ')
aluno3 = input('Digite o nome do terceiro aluno a ser sorteado: ')
aluno4 = input('Digite o nome do quarto aluno a ser sorteado: ')
aluno5 = input('Digite o nome do quinto aluno a ser sorteado: ')
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
