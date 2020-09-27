# DESAFIO 086
# ESTRUTURA LISTAS 02

# CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3
# E PREENCHA COM VALORES LIDOS PELO TECLADO
# NO FINAL, MOSTRE A MATRIZ FORMATADA

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição {linha} {coluna}:  '))
print('-=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^7}]', end='')
    print()
