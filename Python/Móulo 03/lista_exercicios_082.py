# DESAFIO 083
# ESTRUTURA LISTA

# CRIE UM PROGRAMA QUE VAI LEVAR VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA
# DEPOIS DISSO CRIE DUAS LISTAS
# UMA CONTENDO NÚMEROS PARES E OUTRA CONTENDO NÚMEROS IMPARES
# AO FINAL MOSTRE AS TRÊS LISTAS
# UMA DE PARES
# UMA DE IMPARES
# E UMA CONJUNTA

numeros = []
numeros_pares = []
numeros_impares = []

while True:
    elemento = int(input('Digite um número: '))
    numeros.append(elemento)
    if elemento % 2 == 0:
        numeros_pares.append(elemento)
    else:
        numeros_impares.append(elemento)
    continuar = str(input('Deseja continuar adicionando números: [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        print('Dados incorretos!')
        continuar = str(input('Digite S para continuar e N para sair: ')).upper().strip()
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'Essa é a Lista com todos os valores: {numeros}!')
print(f'Essa é a Lista dos pares: {numeros_pares}!')
print(f'Essa é a Lista dos impares: {numeros_impares}!')
