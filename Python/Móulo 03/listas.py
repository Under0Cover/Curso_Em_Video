# LISTAS
# FASE 17

# --- TEORIA COMENTADA ---

# RELEBRANDO A TEORIA DAS TUPLAS
# USO DE PARÊNTESES
# A CHAVE COMEÇA PELO NÚMERO 0
# A IMUTABILIDADE DA TUPLA

# AS LISTAS ACEITAM MUTABILIDADE E AINDA POSSUEM ALGUNS COMANDOS ESPECIAIS
# NA DECLARAÇÃO A ÚNICA MUDANÇA ATÉ AGORA SÃO OS COLCHETES

# EXEMPLO:

lanche_tupla = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche_tupla)
print(lanche)
print('-=-' * 10)

# NA TUPLA O COMANDO ABAIXO DÁ ERRO
# lanche_tupla[3] = ('Picolé')
print(lanche_tupla)
# NA LISTA O COMANDO É VÁLIDO:
lanche[3] = 'Picolé'
print(lanche)
print('-=-' * 10)

# ESSAS SÃO AS PRINCIPAIS DIFERENÇAS
# DAQUI PRA FRENTE VAMOS TRATAR SÓ AS LISTAS
# JÁ QUE A TUPLA NÃO SE ENCAIXA DAQUI PRA FRENTE

# ADICIONANDO ELEMENTOS NO FINAL DA LISTA
lanche.append('Biscoito')
print(lanche)
# ADICIONANDO ELEMENTOS EM QUALQUER LUGAR DA LISTA
lanche.insert(0, 'Cachorro Quente')
# O COMANDO INSERT INSERE NA POSIÇÃO DECLARADA O NOVO ELEMENTO
print(lanche)
print('-=-' * 10)

# PARA EXCLUIR ALGUM ELEMENTO DO LISTA TEMOS O COMANDO DEL
del lanche[3]
# VOCÊ INDICA A POSIÇÃO QUE QUER DELETAR
print(lanche)
# O COMANDO POP TAMBÉM PODE SER USADO PARA EXCLUIR
# PORÉM ELE É MAIS USADO PARA ELIMINAR O ÚLTIMO ELEMENTO
lanche.pop(3)
print(lanche)
# PARA ELEMINAR O ÚLTIMO ELEMENTO
# lanche.pop()
print('-=-' * 10)

# OUTRO COMANDO QUE FUNCIONA PARA APAGAR ELEMENTOS É O REMOVE
# O REMOVE APAGA O ELEMENTO PELO NOME, NÃO PELA CHAVE
# PORÉM SE O ELEMENTO NÃO ESTIVER DENTO DA LISTA INDICADA O PROGRAMA RETORNA UM ERRO
# ISSO FAZ ELE SER MUITO USADO DENTRO DE IFS
# lanche.remove('Pizza')

if 'Pizza' in lanche:
    lanche.remove('Pizza')
    print('Removi a Pizza dos Lanches!')
else:
    print('Não há Pizza nos Lanches!')
if 'Hamburguer' in lanche:
    lanche.remove('Hamburguer')
    print('Removi Hamburger de Lanche!')
else:
    print('Não há Hamburguer nos Lanches!')
print(lanche)
print('-=-' * 10)

# TAMBÉM PODEMOS CRIAR UMA LISTA DA SEGUINTE FORMA:
valores = list(range(4, 11))
print(valores)
print('-=-' * 10)

# CASO NÃO QUEIRA O USO DO RANGE, POR CONTA DOS VALORES
# PODE-SE USAR DE OUTRA FORMA:

outros_valores = [8, 2, 5, 4, 9, 3, 0]
print(outros_valores)
# CASO HAJA A NECESSIDADE DE COLOCAR ESSES NÚMEROS EM ORDEM UTILIZA O SORT
outros_valores.sort()
print(outros_valores)
# CASO HAJA A NECESSIDE DE COLOCAR EM ORDEM INVERSA BASTA FAZER ASSIM:
outros_valores.sort(reverse=True)
print(outros_valores)
# PARA SABER O TAMANHO DA LISTA
print(f'Essa lista tem {len(outros_valores)} elementos')
# ESSA É A QUANTIDADE DE ITENS DA LISTA
print('-=-' * 10)

# UM FATO CURIOSO SOBRE INSERT E REMOVE
# COMO OS DOIS ELEMENTOS PODEM CONTER CHAVES
# PODE HAVER MAIS DE UM ELEMENTO REPETIDO
print(outros_valores)
outros_valores.insert(1, 8)
# VOU INSERIR O NÚMERO 8 NA CHAVE 1
# E VÃO TER DOIS NÚMEROS 8
print(outros_valores)
# AGORA EXISTE DOIS NÚMEROS 8
# UM NA CHAVE 1
# UM NA CHAVE 2
# CASO SEJA DADO UM REMOVE, ELE IRÁ REMOVER O PRIMEIRO ITEM
# DEIXANDO O SEGUNDO INTEIRO
outros_valores.remove(8)
print(outros_valores)
print('-=-' * 10)
# DÁ PRA REMOVER O SEGUNDO VALOR COM OS LAÇOS

# EXEMPLOS DE FORMATAÇÃO DA LISTA
# POSSO COMEÇAR UMA LISTA VAZIA DE DUAS FORMAS
numeros = []
letras = list()
print(numeros)
print(letras)
numeros.append(5)
numeros.append(9)
numeros.append(4)
# USANDO O FOR
for n in numeros:
    print(f'{n}...', end=' ')
print(' ')
# MELHORANDO O FOR MOSTRANDO ELEMENTOS E CHAVES
for c, n in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {n}!')
print('Cheguei ao final da Lista de Números!')
# TAMBÉM PODE SE USAR UM FOR PEDINDO OS ELEMENTOS PELO TECLADO
for cont in range(0, 5):
    letras.append(str(input('Digite uma letra: ')).upper().strip())
for c, v in enumerate(letras):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da Lista de Letras!')
print('-=-' * 10)

# ITEM CURIOSO DO PYTHON E DAS LISTAS
# IMAGINE A CRIAÇÃO DE UMA LISTA
lista_a = [2, 3, 4, 7]
lista_b = lista_a
print(f'Essa é a Lista A: {lista_a}!')
print(f'Essa é a Lista B: {lista_b}!')
# ENTENDEMOS QUE AMBAS AS LISTAS SÃO IGUAIS
# AGORA IMAGINE QUE VAMOS MEXER NA LISTA B
# VAMOS ALTERAR ALGUM VALOR DESSA LISTA
lista_b[2] = 8
print(f'Essa é a Lista B: {lista_b}!')
# PORÉM QUANDO VOCÊ FAZ UMA IGUALDADE NO PYTHON
# NÃO É SÓ UMA CÓPIA, É COMO UM ATALHO
# MEXE EM UMA, MEXE NAS DUAS
print(f'Essa é a Lista A: {lista_a}!')
print('-=-' * 10)
# HÁ UMA ALTERNATIVA MUITO BOA PARA ESSA DIDÁTICA
lista_c = [2, 3, 4, 7]
lista_d = lista_c[:]
print(f'Essa é a Lista C: {lista_c}!')
print(f'Essa é a Lista D: {lista_d}!')
# AQUI NÃO SE CRIA UM VÍNCULO COM A OUTRA LISTA
# CRIA-SE UMA CÓPIA DOS ELEMENTOS DA OUTRA LISTA
# E SE FOR FEITA ALTERAÇÕES EM UMA LISTA, A OUTRA PERMANECE INTACT
lista_d[2] = 8
print(f'Essa é a Lista C: {lista_c}!')
print(f'Essa é a Lista D: {lista_d}!')
