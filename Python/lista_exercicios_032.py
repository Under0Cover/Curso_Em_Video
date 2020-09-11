# DESAFIO 031
# ANO BISSEXTO

# CRIE UM PROGRAMA QUE LEIA O ANO E DIGA SE ELE É BISSEXTO OU NÃO

ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {}, é BISSEXTO!!!'.format(ano))
else:
    print('O ano de {}, não é BISSEXTO!!!'.format(ano))

# RECEBENDO O ANO ATUAL DO SISTEMA
'''
from datetime import date
ano = date.today().year
'''