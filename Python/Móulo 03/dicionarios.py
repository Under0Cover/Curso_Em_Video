# DICIONÁRIOS

# --- TEORIA ---

# RELEMBRANDO LISTAS E TUPLAS
'''
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

# OS DICIONÁRIOS PERMITEM PERSONALIZAR OS INDICES PARA LITERAIS
# TUPLAS SÃO DECLARADAS POR PARÊNTESES
# LISTAS SÃO DECLARADAS POR COLCHETES
# JÁ OS DICIONARIOS SÃO DECLARADAS POR CHAVES

dados = dict()
dados = {'Nome':'Pedro', 'Idade':25}
print(dados['Nome'])
print(dados['Idade'])

# COMO ADICINAR UM NOVO ELEMENTO NO DICIONÁRIO?
# O APPEND NÃO FUNCIONA NO DICIONÁRIO
# BASTA FAZER ASSIM:
dados['Sexo'] = 'M'

# PARA APAGAR DADOS EM DICIONÁRIO:
del dados ['Idade']

# CRIAR UM DICIONÁRIO PARA GUARDAR NOMES DE FILMES
filme = {'Titulo': 'Star Wars', 'Ano': 1977, 'Diretor': 'George Lucas'}

# PARA VISUALIZAR OS VALORES DIGITADOS
print(filme.values())
# PARA VISUALIZAR AS CHAVES
print(filme.keys())
# PARA VISUALIZAR A ESTRUTURA COMPLETA
print(filme.items())

# UTILIZANDO O FOR NA ESTRUTURA
for keys, values in filme.items():
    print(f'O {keys} é {values}')

# --- PRÁTICA ---

pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(pessoas)
print(pessoas['Nome'])
print(pessoas['Idade'])

# PRINT FORMATADO
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos!')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['Nome'] = 'Leandro'
for keys in pessoas.keys():
    print(keys)
for values in pessoas.values():
    print(values)
for keys, values in pessoas.items():
    print(f'{keys} = {values}')
pessoas['Peso'] = 98.5
for keys, values in pessoas.items():
    print(f'{keys} = {values}')

# UMA LISTA COM DICIONÁRIOS DENTRO
brasil = []
estado_rio = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado_sp = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado_rio)
brasil.append(estado_sp)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1])
print(brasil[1]['Sigla'])
'''

estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # DIFERENTE DA LISTA QUE USAMOS O [:] PARA COPIAR OS DADOS
    # EM DICIONÁRIOS USAMOS .copy()
    brasil.append(estado.copy())
for estado in brasil:
    print(estado)
    