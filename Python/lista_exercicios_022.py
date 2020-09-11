# DESAFIO 022
# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

# A) O NOME COM TODAS AS LETRAS MAIÚSCULAS
nome_completo = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em MAIÚSCULAS é {}'.format(nome_completo.upper()))

# B) O NOME COM TODAS AS LETRAS MINÚSCULAS
print('Seu nome em todas minúsculas é {}'.format(nome_completo.lower()))

# C) QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
print('Seu nome tem ao todo {} letras'.format(len(nome_completo)-nome_completo.count(' ')))
# FORMATANDO POR CAUSA DAS CHAVES
# LEN PRA SABER O TAMANHO DA STRING
# MENOS OS ESPAÇOS VAZIOS DA STRING

# D) QUANTAS LETRAS TEM O PRIMEIRO NOME
print('Seu primeiro nome tem {} letras'.format(nome_completo.find(' ')))


# PODE SER FEITO COM O SPLIT
# JÁ APROVEITA PRA SEPARAR O NOME E DAR O TAMANHO DO PRIMEIRO NOME
# separador = nome_completo.split()
# print('Seu primeiro nome é {} e ele tem {} letras'.format(separador[0], len(separador[0])))
