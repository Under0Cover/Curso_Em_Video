# DESAFIO 061
# ESTRUTURA WHILE

# REFAÇA O EXERCÍCIO 051
# O EXERCÍCIO DE PROGRESSÃO ARITMÉTICA
# LENDO O TERMO E A RAZÃO
# E MOSTRANDO OS 10 PRIMEIROS TERMOS
# USANDO A ESTRUTURA WHILE

print('Cálculo de Progressão Aritmética')
prim_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da Progressão: '))

termo = prim_termo
contador = 1

while contador <= 10:
    print('{} -'.format(termo), end=' ')
    termo += razao
    contador += 1
print('\nFIM DO PROGRAMA')
