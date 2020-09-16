# ESTRUTURA WHILE
# --- TEORIA ---

# ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

''''
ENQUANTO NÃO CHEGA NA MAÇA:
    PASSO
PEGA

WHILE NOT MAÇA:
    PASSO
PEGA

# ENQUANTO VOCÊ SABE O LIMITE, MELHOR USAR O FOR
# SE VOCÊ DESCONHECE O NÚMERO DE AÇÕES, USE O WHILE

ENQUANTO NÃO CHEGA NA MAÇA:
    SE TIVER CHÃO:
        PASSO
    SE TIVER BURACO:
        PULA
    SE TIVER MOEDA:
        PEGA
PEGA

WHILE NOT MAÇA:
    IF CHÃO:
        PASSO
    IF BURACO:
        PULA
    IF MOEDA:
        PEGA
PEGA

# --- NA PRÁTICA ---

for c in range(1,10):
    print(c)
print('FIM')
# UM FOR SIMPLES QUE VAI ATÉ 10
# IMPRIMINDO OS NÚMEROS


c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
# MESMO EXEMPLO DO ANTERIOR USANDO O WHILE


for c in range(1,5):
    n = int(input('Digite um valor: '))
print('FIM')
# UM FOR PARA A DIGITAÇÃO DE 5 VALORES


n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
# UM WHILE USADO PRA FAZER O MESMO EXEMPLO ANTERIOR
# PORÉM A SAÍDA DO WHILE É N = 0


r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: '))
print('FIM')
# AQUI COM A OPÇÃO DE SAIR


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        # N != 0 PARA 0 NÃO SER CONSIDERADO PAR
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
# AQUI UM PROGRAMA SIMPLES PARA IMPRIMIR A QUANTIDADE DE PARES E ÍMPARES
'''
