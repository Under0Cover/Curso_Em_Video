# DESAFIO 076
# TUPLAS

# CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS NA SEQUÊNCIA
# NO FINAL MOSTRE UMA LISTAGEM DE PREÇOS
# ORGANIZANDO OS DADOS DE FORMA TABULAR

tabela_precos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
                 'Estojo', 25, 'Transferidor', 4.50, 'Compasso', 9.99,
                 'Mochila', 120.55, 'Canetas', 12.50, 'Livro', 34.99)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
# A FORMATAÇÃO DA LISTAGEM DE PREÇOS É:
# ^  -> CENTRALIZADO
# 40 -> 40 CARACTERES
print('-' * 40)
for pos in range(0, len(tabela_precos)):
    # A FORMATAÇÃO DO FOR É:
    # FOR POS IN RANGE ->> NORMAL! PARA POSIÇÃO EM RANGE DE 0 ATÉ O TAMANHO DA TABELA_PRECOS
    if pos % 2 == 0:
        # A POSIÇÃO DIVIDA COM RESULTADO ZERO NA DIVISÃO DE 2, SIGNIFICA QUE VAMOS PEGAR AS POSIÇÕES PARES
        # ESSAS POSIÇÕES SÃO AS DOS ITENS
        print(f'{tabela_precos[pos]:.<30}', end='')
        # A FORMATAÇÃO DO PRINT É:
        # VAI MOSTRAR O VALOR QUE ESTÁ NA POSIÇÃO PAR (OS ITENS)
        # : ->> PREFIXO PARA FORMATAÇÕES
        # . ->> VAI ADICIONAR PONTOS
        # <  ->> PREFIXO PARA ALINHAR A ESQUERDA
        # 30 ->> 30 CARACTERES
    else:
        print(f'R${tabela_precos[pos]:>7.2f}')
        # A FORMATAÇÃO DO PRINT É:
        # VAI MOSTRAR O VALOR QUE ESTÁ NA POSIÇÃO IMPART (OS VALORES)
        # :  ->> PREFIXO PARA FORMATAÇÕES
        # >  ->> ALINHA A DIREITA
        # 7  ->> 07 CARACTERES
        #.2f ->> ADICIONAR DUAS CASAS DECIMAIS APÓS O PONTO
print('-' * 40)
