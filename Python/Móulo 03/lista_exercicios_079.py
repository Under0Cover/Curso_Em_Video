# DESAFIO 079
# ESTRUTURA DE LISTAS

# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES
# E CADASTRE EM UMA LISTA
# CASO O NÚMERO JÁ EXISTA NÃO SERÁ ADICIONADO!
# NO FINAL EXIBA TODOS OS VALORES ÚNICOS DIGITADOS EM ORDEM CRESCENTE

numeros = []
while True:
    aprovacao = int(input('Digite um número: '))
    if aprovacao in numeros:
        print('Esse número já existe na Lista!')
    else:
        numeros.append(aprovacao)
        print('Valor adicionado!')
    valor = str(input('Quer adicionar outro número? [S/N]: ')).upper().strip()[0]
    while valor not in 'SN':
        print('Dados inválidos!')
        valor = str(input('Digite (S) para adicionar outro número'
                          'e (N) para ver a sua Lista: ')).upper().strip()[0]
    if valor == 'N':
        break
numeros.sort()
print(f'Os números digitados em ordem crescente são: {numeros}!')
