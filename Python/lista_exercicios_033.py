# DESAFIO 033
# QUAL NÚMERO É MAIOR?

# CRIE UM PROGRAMA QUE RECEBA 3 NÚMEROS E DIGA QUAL É O MAIOR E QUAL É O MENOR

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite o terceiro número: '))
num_menor = numero1
if numero2 < numero1 and numero2 < numero3:
    num_menor = numero2
if numero3 < numero1 and numero3 < numero2:
    num_menor = numero3
num_maior = numero1
if numero2 > numero1 and numero2 > numero3:
    num_maior = numero2
if numero3 > numero1 and numero3 > numero2:
    num_maior = numero3
print('O maior valor é {} e o menor valor é {}'.format(num_maior, num_menor))
