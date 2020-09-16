# DESAFIO 054
# ESTRUTURA FOR

# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE 07 PESSOAS
# MOSTRE QUANTAS PESSOAS SÃO MENORES DE IDADE
# MOSTRE QUANTAS PESSOAS SÃO MAIORES DE IDADE
# CONSIDERANDO A MAIORIDADE COMO 21 ANOS

from datetime import date
ano_sistema = date.today().year
pess_maior = 0
pess_menor = 0

for c in range(0, 7):
    info_pess = int(input('Informe o ano de Nascimento da {}ª Pessoa: '.format(c + 1)))
    idade = ano_sistema - info_pess
    if idade >= 21:
        pess_maior += 1
    else:
        pess_menor += 1
print('Há {} pessoas que são maiores de idade!'.format(pess_maior))
print('Há {} pessoas que são menores de idade!'.format(pess_menor))
