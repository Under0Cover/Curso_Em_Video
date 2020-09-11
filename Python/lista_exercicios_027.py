# DESAFIO 027
# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E FAÇA:

nome_completo = str(input('Digite o seu nome completo: ')).strip()
print('Que bom que você veio...')
nome = nome_completo.split()

# A) MOSTRANDO O PRIMEIRO NOME
print('O seu primeiro nome é {}'.format(nome[0]))

# B) MOSTRANDO O ÚLTIMO NOME
print('Seu último nome é {}'.format(nome[len(nome)-1]))
