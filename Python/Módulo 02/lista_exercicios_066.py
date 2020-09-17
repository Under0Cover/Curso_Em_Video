# DESAFIO 066
# ESTRUTURA WHILE COM BREAK

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS
# O PROGRAMA DEVE PARAR QUANDO O USUÁRIO DIGITAR 999
# NO FIM, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS
# E QUAL A SOMA ENTRE ELES
# OBS: O NÚMERO 999 NÃO DEVE SER CONSIDERADO NA SOMA

soma = contador = 0

while True:
    numero = int(input('Digite um número para ser somado [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'A quantidade de valores digitado foi {contador}.')
print(f'A soma de todos os números é {soma}.')
