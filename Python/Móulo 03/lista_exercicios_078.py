# DESAFIO 078
# ESTRUTRA LISTAS

# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA.
# NO FINAL MOSTRE O MAIOR E O MENOR VALOR
# ALÉM DISSO TAMBÉM MOSTRE AS SUAS CHAVES NA LISTA

numeros = []
for contador in range(0, 5):
    numeros.append(int(input(f'Digite o valor da posição {contador}: ')))
print(f'Essa é a sua Lista de números: {numeros}!')
print(f'O maior número digitado foi o {max(numeros)} e ele está na posição: ', end='')
# A FUNÇÃO ENUMARATE RETORNA CADA ÍNDICE ASSOCIADO AO SEU VALOR
for indice, valor in enumerate(numeros):
    if valor == max(numeros):
        print(f'{indice}. ', end='')
print('')
print(f'O menor número digitado foi o {min(numeros)} e ele está na posição: ', end='')
for indice, valor in enumerate(numeros):
    if valor == min(numeros):
        print(f'{indice}. ', end='')
