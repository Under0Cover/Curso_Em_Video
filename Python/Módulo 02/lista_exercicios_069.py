# DESAFIO 069
# ESTRUTURA WHILE COM BREAK

# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS
# A CADA PESSOA CADASTRADA, ELA DEVERÁ PERGUNTAR SE O USUÁRIO QUER CONTINUAR
# NO FINAL MOSTRE 3 RETORNOS:
# QUANTAS PESSOAS TEM MAIS DE 18 ANOS
# QUANTOS HOMENS FORAM CADASTRADOS
# QUANTAS MULHERES TEM MENOS DE 20 ANOS

from datetime import date
ano_sistema = date.today().year
# JÁ PRA CALCULAR A IDADE
cadastro = 'S'
# ARRUMANDO UMA FLAG
num_homens = 0
# CÁLCULO PARA NÚMERO DE HOMENS
num_mulh_menos_20 = 0
# CÁLCULO PARA MULHERES MENORES DE 20 ANOS
maior_idade = 0
# CÁLCULO PARA PESSOAS COM MAIS DE 18 ANOS

while cadastro == 'S':
    ano_nasc = int(input('Qual o ano do nascimento: '))

    sexo = str(input('Qual o sexo da pessoa [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        print('Dados inválidos!!')
        sexo = str(input('Por favor informe (M) para MASCULINO e (F) para FEMININO: ')).upper().strip()[0]
        # CERTIFICANDO DE A PESSOA ESCOLHER OS SEXO DISPONÍVEIS
    if sexo == 'M':
        num_homens += 1
        # SOMANDO +1 HOMEM QUANDO SEXO É MASCULINO

    # O PROGRAMA NÃO INFORMOU A NECESSIDADE DE PEDIR O NOME

    idade = ano_sistema - ano_nasc
    # CALCULANDO A IDADE DA PESSOA
    if idade >= 18:
        maior_idade += 1
    # SOMANDO +1 QUANDO A IDADE É MAIS DE 18 ANOS
    print('-=-' * 20)
    print('Dados cadastrados com sucesso!')
    print('-=-' * 20)
    if sexo == 'F' and idade < 20:
        num_mulh_menos_20 += 1
        # SOMANDO +1 MULHER COM IDADE MENOR DE 20 ANOS

    cadastro = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).upper().strip()[0]
    # INSERINDO A FLAG DE EXIT
    print('-=-' * 20)

print(f'O número de pessoas com mais de 18 anos é {maior_idade}')
print(f'A quantidade de homens cadastradas é {num_homens}')
print(f'A quantidade de mulheres com menos de 20 anos é {num_mulh_menos_20}')
