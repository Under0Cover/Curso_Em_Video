# DESAFIO 052
# NÚMERO PRIMO

# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO PRIMO

numero = int(input('Digite um número: '))
divisivel = 0
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[34m', end='')
        divisivel += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(contador), end='')
print(' ')
print('\n\033[31mO número {} foi divisível {} vezes'.format(numero, divisivel))
if divisivel == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')
