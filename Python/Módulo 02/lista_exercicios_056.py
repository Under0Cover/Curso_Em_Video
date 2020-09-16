# DESAFIO 056
# ESTRUTURA FOR

# DESENVOLVA UM PROGRAMA QUE LEIA
# NOME, IDADE E SEXO DE 4 PESSOAS
# RETORNE 03 RESULTADOS:
# 1) A MÉDIA DE IDADE DO GRUPO
# 2) QUAL É O NOME DO HOMEM MAIS VELHO
# 3) QUANTAS MULHERES TEM MENOS DE 20 ANOS

mulher_menos_vinte = 0
maior_idade_homem = 0
nome_h_velho = ''
media_idade = 0
soma_idades = 0
for pessoas in range(1, 5):
    print('-=-' * 20)
    print(' INFORMAÇÕES DA {}ª PESSOA '.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma_idades += idade
    if pessoas == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_h_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_h_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_menos_vinte += 1


print(' ')
# QUAL É A MÉDIA DAS IDADES?
media_idade = soma_idades / pessoas
print('A média de idade das {} pessoas é de {:.1f}'.format(pessoas, media_idade))
# QUAL É A IDADE E O NOME DO HOMEM MAIS VELHO?
print('O {} é o homem mais velho e tem {} anos de idade'.format(nome_h_velho, maior_idade_homem))
# QUANTAS MULHERES TEM MENOS DE 20 ANOS?
print('{} mulheres tem menos de 20 anos de idade'.format(mulher_menos_vinte))



