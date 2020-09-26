# DESAFIO 081
# ESTRUTURA FILA

# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR ELES EM UMA LISTA
# DEPOIS DISSO RETORNE:
# A) QUANTOS NÚMEROS FORAM DIGITADOS
# B) A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE
# C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        print('Dados inválidos!')
        continuar = str(input('Digite S para continuar e N para sair: ')).upper().strip()
    if continuar == 'N':
        break
print(f'Foram digitados {len(numeros)} números!')
print(f'A Lista digitada foi: {numeros}!')
numeros.sort(reverse=True)
print(f'Em ordem decrescente a Lista fica: {numeros}!')
if 5 in numeros:
    print(f'O número 5 foi digitado e está na Lista!')
else:
    print('O número 5 não foi digitado e não está na Lista!')
