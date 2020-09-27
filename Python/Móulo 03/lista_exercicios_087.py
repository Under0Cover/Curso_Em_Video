# DESAFIO 087
# ESTRUTURA LISTAS 02

# APRIMORE O DESAFIO ANTERIOR
# MOSTRANDO NO FINAL
# A) A SOMA DE TODOS OS VALORES PARES
# B) A SOMA DOS VALORES DA TERCEIRA COLUNA
# C) O MAIOR VALOR DA SEGUNDA LINHA

# EXATAMENTE O MESMO CÓDIGO DO EXERCÍCIO ANTERIOR
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_ter_col = maior_seg_lin = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição {linha} {coluna}:  '))
print('-=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^7}]', end='')
        # A VERIFICACAO PARA IDENTIFICAR PARES E IMPARES
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é {soma_pares}!')
# PERCORRENDO AS LINHAS PARA SOMAR A TERCEIRA COLUNA
for linha in range(0, 3):
    soma_ter_col += matriz[linha][2]
print(f'A soma da terceira coluna é {soma_ter_col}!')
# PERCORRENDO AS COLUNAS PARA SABER O MAIOR VALOR DA SEGUNDA LINHA
for coluna in range(0, 3):
    if coluna == 0:
        maior_seg_lin = matriz[1][coluna]
    elif matriz[1][coluna] > maior_seg_lin:
        maior_seg_lin = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior_seg_lin}!')
