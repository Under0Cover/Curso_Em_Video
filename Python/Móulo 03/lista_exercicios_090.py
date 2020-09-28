# DESAFIO 090
# ESTRUTURA DICIONÁRIOS

# FAÇA UM PROGRAMA QUE LEIA O NOME E A MÉDIA DE UM ALUNO
# GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO
# NO FINAL MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA

print('-=' * 20)
print('Boletim Escolar')
print('-=' * 20)
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do Aluno: '))
aluno['Media'] = float(input(f'Digite a média do Aluno {aluno["Nome"]}: '))

if aluno['Media'] > 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'
print('-=' * 20)
for keys, values in aluno.items():
    print(f'{keys} é igual a {values}')