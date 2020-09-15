# LAÇOS DE REPETIÇÕES
# ESTRUTURA DE REPETIÇÃO FOR

# --- TEORIA  ---

# LAÇO DE REPETIÇÃO COM CONTROLE DE SAÍDA
# EXEMPLO 01
for c in range(1, 10):
    passo
pega

# EXEMPLO 02
for c in range(0, 3):
    passo
    pula
passo
pega

# EXEMPLO 03
for c in range(0, 3):
    if moeda
        pega
    passo
    pula
if moeda:
    pega
passo
pega

# --- PRÁTICA ---

# PRINT 'OI' 6x
for c in range(1, 6):
    print('Oi')
print('FIM!')

# PRINT 'OI' 'FIM' 6x
for c in range(1, 6):
    print('OI')
    print('FIM')

# PRINT 'C' DE 1 ATÉ 5
# PRINT 'FIM'
for c in range(1, 6):
    print(c)
print('FIM')

# PRINT 'C' DE 1 ATÉ 6
# PRINT 'FIM'
for c in range(1, 7):
    print(c)
print('FIM')

# PRINT 'FIM'
for c in range(6, 0):
    print(c)
print('FIM')

# PARA PRINT DE 6 ATÉ 0
# PRINT 'FIM'
# NO 0 ELE PARA E NÃO DÁ PRINT
for c in range(6, 0, -1):
    print(c)
print('FIM')

# PRINT 'C' DE 0 ATÉ 6
# PRINT 'FIM'
# PRINT 'C' DE 2 EM 2
for c in range(0, 7, 2):
    print(c)
print('FIM')

# RECEBE UM NÚMERO DO USUÁRIO
# N+1 É PRA DAR PRINT ATÉ O NÚMERO QUE O USUÁRIO INFORMOU
num = int(input('Digite um número: '))
for c in range(0, num+1):
    print(c)
print('FIM')

# VOU RECEBER O INÍCIO, O FIM E O PASSO DO USUÁRIO
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print('FIM')

# USANDO UM FOR PARA PEDIR VALORES REPETIDAS VEZES
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')

# USANDO UM FOR PARA RECEBER VÁRIOS NÚMEROS E SOMAR
soma = 0
for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero
    # EM PYTHON:
    # SOMA += NUMERO É IGUAL A:
    # SOMA = SOMA + NUMERO
print('A soma de todos os valores é {}'.format(soma))
