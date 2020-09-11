# DESAFIO 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

nome_completo = str(input('Digite o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome_completo.upper()))

