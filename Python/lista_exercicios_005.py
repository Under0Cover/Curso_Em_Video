# DESAFIO 005
# IMPRIMIR O SUCESSOR E O ANTECESSOR DE UM NOVO DADO

numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor de {} é {} e o antecessor de {} é {}'.format(numero, sucessor, numero, antecessor))

"""OUTRA FORMA DE FAZER É:
PRINT('ANALISANDO O VALOR {}, SEU ANTECESSOR É {} E O SUCESSOR É {}'.FORMAT(VARIAVEL, (VARIVAVEL-1), (VARIAVEL+1)))"""