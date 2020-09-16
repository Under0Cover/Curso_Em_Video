# DESAFIO 053
# ESTRUTURA FOR
# DESAFIO DO PALÍNDROMO

# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER
# E DIGA SE ELA É UM PALÍNDROMO
# DESCONSIDERANDO OS ESPAÇOS

frase = str(input('Digite uma frase: ')).strip().upper()
# TIRANDO OS ESPAÇOS DESNECESSÁRIOS COM STRIP
# COLOCANDO TUDO EM MAISCÚLAS COM UPPER
palavras = frase.split()
# DIVIDINDO A FRASE EM PALAVRAS COM SPLIT
tudo_junto = ''.join(palavras)
# JUNTOU TODAS AS PALAVRAS, DESCONSIDERANDO OS ESPAÇOS
# ESSE JOIN JUNTA AS PALAVRAS
# TUDO ATÉ AGORA FOI FEITO PRA TIRAR OS ESPAÇOS E JUNTAR A STRING
inverso = ''
# NO CASO DO PYTHON, NÃO SERIA NECESSÁRIO ESSE FOR
# BASTA NO INVERSO = ''
# COLOCAR O COMANDO: INVERSO = JUNTO[::-1]
# E O FOR PODE SER RETIRADO
for letra in range(len(tudo_junto) - 1, -1, -1):
    # FOR PERCORRENDO TUDO_JUNTO E LENDO DE TRÁS PARA FRENTE
    # POR ISSO OS NEGATIVOS
    inverso += tudo_junto[letra]
print('Você digitou {} e o inverso é {}'.format(tudo_junto, inverso))
if inverso == tudo_junto:
    # TODO AQUELE TRABALHO DE QUEBRAR, TIRAR OS ESPAÇOS E UNIR
    # FOI PARA FAZER ESSA COMPARAÇÃO
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
