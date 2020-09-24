# DESAFIO 072
# TUPLAS

# CRIE UM PROGRAMA QUE TENHA UMA TUPLA PREENCHIDA
# COM CONTAGEM POR EXTENSO DE 0 ATÉ 20
# O PROGRAMA DEVERÁ LER UM NUMERO PELO TECLADO
# E MOSTRÁ-LO POR EXTENSO

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
jogar_novamente = 'S'
while jogar_novamente == 'S':
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {contagem[numero]}')
    jogar_novamente = str(input('Você deseja jogar novamente? [S/N]:  ')).upper().strip()
    if jogar_novamente == 'S':
        print('-=-' * 10 + ' Recomeçando ' + '-=-' * 10)
    else:
        print('-' * 73)
        print('Obrigado por participar!')
