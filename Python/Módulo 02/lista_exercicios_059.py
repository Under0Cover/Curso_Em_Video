# DESAFIO 059
# ESTRUTURA WHILE

# CRIE UM PROGRAMA QUE LEIA DOIS VALORES
# DEPOIS MOSTRE UM MENU NA TELA COM AS OPÇÕES:
# 1) SOMAR
# 2) MULTIPLICAR
# 3) MAIOR
# 4) NOVOS NÚMEROS
# 5) SAIR DO PROGRAMA

from time import sleep

sair = 'N'
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
while sair != 'S':
    print('Escolha uma opção: ')
    print('( 1 ) - Somar: ')
    print('( 2 ) - Multiplicar: ')
    print('( 3 ) - Maior número: ')
    print('( 4 ) - Novos números: ')
    print('( 5 ) - Sair do programa: ')
    opcao = int(input('Opção desejada: '))
    if opcao == 1:
        soma = numero1 + numero2
        print('A soma do número {} e do número {} é igual a {}'.format(numero1, numero2, soma))
        sleep(2)
        print('-=-' * 15)
    elif opcao == 2:
        multiplica = numero1 * numero2
        print('A multiplicação do número {} e do número {} é igual a {}'.format(numero1, numero2, multiplica))
        sleep(2)
        print('-=-' * 15)
    elif opcao == 3:
        if numero1 > numero2:
            print('O número {} é maior que o número {}'.format(numero1, numero2))
            sleep(2)
            print('-=-' * 15)
        elif numero2 > numero1:
            print('O número {} é maior que o número {}'.format(numero2, numero1))
            sleep(2)
            print('-=-' * 15)
        else:
            print('Os números são iguais')
            sleep(2)
            print('-=-' * 15)
    elif opcao == 4:
        print('Digite novos números.')
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
        sleep(2)
        print('-=-' * 15)
    elif opcao == 5:
        sair = str(input('Deseja sair do programa? [S/N]: ')).upper()
        sleep(2)
        print('-=-' * 15)
    else:
        print('Opção inválida, por favor, tente novamente!')
        sleep(2)
        print('-=-' * 15)
