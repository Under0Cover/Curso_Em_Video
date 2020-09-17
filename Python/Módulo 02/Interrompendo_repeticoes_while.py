# CONTINUAÇÃO DOS LAÇOS DE REPETIÇÃO

# NORMALMENTE SÃO TRÊS TIPOS DE LAÇOS DE REPETIÇÕES
# FOR
# WHILE
# DO-WHILE (OU REPEAT)

# NO PYTHON SÃO DUAS
# JÁ ATÉ ESTUDADAS
# FOR
# WHILE
# MAS EXISTEM FORMAS DE SIMULAR O DO-WHILE

# --- TEORIA ---

# RESUMO AULA 14

'''ENQUANTO NÃO CHEGA NA MAÇA:
        SE TEM PISO:
            PASSO
        SE TEM ABISMO:
            PULA
        SE TEM MOEDA:
            PEGA
TEM MAÇA?
    PEGA'''

# NOVA HISTÓRIA, AGORA COM TROFÉU
'''ENQUANTO VERDADEIRO: # AGORA SEM MAÇA
        SE TEM PISO:
            PASSO
        SE TEM ABISMO:
            PULA
        SE TEM MOEDA:
            PEGA
        SE TEM TROFÉU:
            PULA
            INTERROMPA
PEGA'''

# EM INGLÊS:

'''WHILE TRUE:
    IF PISO:
        PASSO
    IF ABISMO:
        PULA
    IF MOEDA:
        PEGA
    IF TROFÉU:
        PEGA
        *BREAK*
PEGA'''

# O COMANDO WHILE FAZ O LOOP GIRAR DE VOLTA PRA CIMA
# O COMANDO BREAK FAZ O LOOP SER INTERROMPIDO E CONTINUAR NA PARTE DE BAIXO

# --- PRÁTICA ---
'''
contador = 1
while contador <= 10:
    print(contador, '...', end=' ')
    contador += 1
print('FIM')
'''

## EXERCÍCIO COMENTADO

# AQUELE EXERCÍCIO DO NÚMERO 999 COM FLAG
# SEM UTILIZAR GAMBIARRAS

soma = 0
# EU TINHA DECLARADO O NÚMERO AQUI EM CIMA
# MAS O PYTHON NÃO CURTE MUITO ESSA PRÁTICA E DÁ "ATENÇÃO"
while True:
    # CRIANDO UM LOOP INFINITO, VISTO QUE O 999 É A NOSSA SAÍDA
    numero = int(input('Digite um número: '))
    if numero == 999:
        # ADICIONANDO A FLAG
        break
        # COMANDO BREAK ANTES DA SOMA
    soma += numero
# print('A soma vale {}.'.format(soma))

# PEP 498
# FSTRINGS

# NO INÍCIO DO CURSO, O PYTHON TINHA OUTRA VERSÃO
# AGORA NO MEIO DO CURSO, A FORMA COMO COLOCAMOS O FORMAT(VARIAVEL) MUDOU

print(f'A soma vale {soma}.')

# EXEMPLOS DE FSTRING

'''
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')                -- NOVO JEITO
print('O {} tem {} anos.'.format(nome, idade))      -- JEITO QUE COMEÇAMOS
print('O %s tem %d anos.' % (nome, idade))          -- JEITO ANTIGO

salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}')
'''