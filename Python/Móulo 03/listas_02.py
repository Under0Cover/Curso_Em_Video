# LISTAS 02
# FASE 18

# -- TEORIA ---

# RELEMBRADO OS PRIMEIROS CONCEITOS DE LISTA
# RELEMBRANDO COMO CRIAR UMA LISTA
# E DIFERENCIADO A LISTA DE UMA TUPLA
'''
dados = list()
# UMA LISTA CHAMADA DADOS ESTÁ CRIADA COMO VAZIA

dados.append('Pedro')
# AQUII ESTÁ ADICIONADO O PRIMEIRO ELEMENTO DA LISTA
dados.append(25)
# ASSIM SUCESSIVAMENTE
# SE EU FIZER ISSO
print(dados[0])
# ELE VAI MOSTRAR O DADO NA CHAVE 0
print(dados[1])
# ASSIM SUCESSIVAMENTE

# AGORA VAMOS TRABALHAR COM LISTAS DENTRO DE LISTAS
# EU VOU CRIAR UMA OUTRA LISTA CHAMADA PESSOAS
pessoas = list()

# EU VOU FAZER UMA CÓPIA DE DADOS DENTRO DE PESSOAS
pessoas.append(dados[:])
# AGORA MINHA CHAVE 0 CONTÉM AS INFORMAÇÕES QUE TINHA EM DADOS
# ASSIM FICA A DECLARAÇÃO DE 3 LISTAS DENTRO DE UMA OUTRA LISTA
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
# ESSE PRINT IRÁ RETORNAR PEDRO
# A CHAVE 0 DE PESSOAS
# A CHAVE 0 DA OUTRA LISTA
print(pessoas[1][1])
# DO MESMO MODO ESSE PRINT IRÁ RETORNAR 19
print(pessoas[2][0])
print(pessoas[1])
# ASSIM SUCESSIVAMENTE

teste = list()
teste.append('Gustavao')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
# ESSE COMANDO FAZ SER COMO UM ÍCONE
# FICA ETERNAMENTE LIGADO E FACIL DE SER CLONADO

# PARA SE CRIAR UMA LISTA COMPLETAMENTE DIFERENTE
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# TAMBÉM POSSO DECLARAR DESSA FORMA
outra_galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# AQUI ELE ME RETORNA TODA A OUTRA GALERA
print(outra_galera)
# AQUI EU SÓ MOSTRO QUEM ESTÁ NA POSIÇÃO 0
print(outra_galera[0])
# AQUI EU SÓ MOSTRO A CHAVE 0 DENTRO DA CHAVE 0 PRINCIPAL
print(outra_galera[0][0])
# PARA MOSTRAR TODOS OS ELEMENTOS DA LISTA PRINCIPAL
for pessoas in outra_galera:
    print(pessoas)
# NESSE OUTRO CASO, SE EU QUISER APENAS OS NOMES EU POSSO FAZER ASSIM:
for pessoas in outra_galera:
    print(pessoas[0])
# DA MESMA FORMA, POSSO FAZER O CONTRÁRIO APENAS PARA AS IDADES:
for idade in outra_galera:
    print(idade[1])
# UM PRINT FORMATADO FICARIA ASSIM:
for pessoas in outra_galera:
    print(f'{pessoas[0]} tem {pessoas[1]} anos de idade!')
'''
# DE FORMA PRÁTICA
# EU VOU PEGAR NOME E IDADE DE TRÊS PESSOAS
# ARMAZENAR TEMPORARIAMENTE NA LISTA DADOS
# E DEPOIS TRANSFERIR PARA GALERA
galera = list()
galera_vazia = list()
dados = list()
for contador in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    galera_vazia.append(dados)
    dados.clear()
print(galera)
print(galera_vazia)
# CASO EU ME ESQUEÇA DO '[:]'
# A LISTA RETORNA VAZIA
# PORQUE EU CRIEI UMA LIGAÇÃO ENTRE DADOS E GALERA VAZIA
# NA LISTA GALERA, EU ESTOU COPIANDO O CONTEUDO

# CONSIDERANDO 21 ANOS COMO MAIORIDADE
# VAMOS USAR UM PRINT PARA MOSTRAR QUEM É MAIOR DE IDADE E QUEM NÃO É
# VAMOS MOSTRAR TAMBÉM A SOMA DOS MAIORES E MENORES DE IDADE
total_maiores = total_menores = 0
# ESSA ESTRUTURA EU SÓ POSSO UTILIZAR PARA VARIAVEIS SIMPLES
# EU NÃO POSSO FAZER ISSO:
# galera = dados = list()
for pessoas in galera:
    if pessoas[1] >= 21:
        print(f'{pessoas[0]} é maior de idade!')
        total_maiores += 1
    else:
        print(f'{pessoas[0]} é menor de idade!')
        total_menores += 1
print(f'O total de maiores de idade é {total_maiores} pessoas!')
print(f'O total de menores de idade é {total_menores} pessoas!')
