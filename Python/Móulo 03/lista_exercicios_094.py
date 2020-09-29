# DESAFIO 094
# ESTRUTURA DICIONÁRIO

# CRIE UM PROGRAMA QUE LEIA O NOME, SEXO E A IDADE DE VÁRIAS PESSOAS
# GUARDANDO TUDO EM UM DICIONÁRIO
# NO FINAL MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS
# B) A MÉDIA DE IDADE DO GRUPO
# C) UMA LISTA COM TODAS AS MULHERES
# D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA

galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite o nome: '))
    while True:
        pessoas['Sexo'] = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERROR!! Por favor, digite apenas M ou F!')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    media = soma / len(galera)
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERROR! Por favor, digite apenas S ou N!')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas!')
print(f'A média das idades das pessoas cadastradas é: {media:5.1f} anos')
print(f'As mulheres cadastradas foram ', end='')
for pessoas in galera:
    if pessoas['Sexo'] == 'F':
        print(f'{pessoas["Nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for pessoas in galera:
    if pessoas['Idade'] >= media:
        for chave, indice in pessoas.items():
            print(f'{chave} = {indice};', end=' ')
print()
print('Programa finalizado!')