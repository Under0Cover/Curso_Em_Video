# DESAFIO 100
# ESTRUTURA FUNÇÕES

# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES
# UMA CHAMADA SORTEIO E OUTRA CHAMADA SOMAPAR()
# A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCA-LOS DENTRO DE UMA LISTA
# A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR

# IMPORTAÇÕES
from random import randint
from time import sleep


# FUNÇÕES
def linha():
    print('-' * 60)


def sortear(lista):
    linha()
    sleep(0.3)
    print('Sorteando 5 valores da Lista: ', end='')
    for contador in range(0, 5):
        sorteado = randint(1, 10)
        lista.append(sorteado)
        sleep(0.8)
        print(f'{sorteado} ', end='')
    print('\nFEITO!')
    linha()


def soma_par(lista):
    linha()
    sleep(0.3)
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}!')
    linha()
    sleep(0.6)



# PROGRAMA PINCIPAL
numeros = list()
sortear(numeros)
sleep(1)
print(numeros)
sleep(1)
soma_par(numeros)