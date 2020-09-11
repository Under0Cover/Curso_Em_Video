# DESAFIO 020
# SORTEANDO UMA ORDEM EM UMA LISTA

from random import shuffle
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
aluno5 = input('Nome do quinto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)