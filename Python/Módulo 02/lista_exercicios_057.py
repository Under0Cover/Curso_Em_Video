# DESAFIO 057
# ESTRUTURA WHILE

# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA
# MAS SÓ ACEITE OS VALORES 'M' OU 'F'
# CASO ERRADO, PEÇA DIGITAÇÃO NOVAMENTE DE UM VALOR VÁLIDO

# MINHA RESOLUÇÃO: 
'''
sair = 'S'
sexo_masc = sexo_fem = 0
while sair == 'S':
    nome = str(input('Digite o seu nome: '))
    ano_nasc = int(input('Digite o seu ano de nascimento: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
            sexo_masc += 1
    elif sexo == 'F':
        sexo_fem +=1
    else:
        print('Valor inválido!')
        print('Por favor refaça o cadastro')
    sair = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')
'''


# RESOLUÇÃO DO PROFESSOR ---=>
sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
# O PROFESSOR QUERIA A VERIFICAÇÃO DO SEXO ANTES MESMO DE DAR CONTINUIDADE NO CADASTRO!
