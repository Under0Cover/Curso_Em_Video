# DESAFIO 085
# ESTRUTURA LISTAS 02

# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE 7 NUMEROS
# E CADASTRE EM UMA LISTA ÚNICA
# POREM DEVE MANTER SEPARADOS OS VALORES PARES E IMPARES
# NO FINAL MOSTRE OS VALORES PARES E IMPARES EM ORDEM CRESCENTE


# COMENTANDO NO EXERCICIO OUTRA FORMA DE FAZER A MESMA ATIVIDADE
numeros = []
# AO INVÉS DE DECLARAR UMA LISTA COMO PAR E UMA COMO IMPAR
# EU POSSO DECLARAR NUMEROS COM DUAS LISTAS
# PRA ISSO UTILIZO O COMANDO:
# numeros = [[], []]
pares = []
impares = []
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o valor da {contador}ª posição: '))
    if valor % 2 == 0:
        pares.append(valor)
        numeros.append(valor)
        pares.sort()
        numeros.sort()
        # NO MOMENTO DA INSERCAO DOS DADOS
        # A FORMA DE FAZER PARA ESSE EXEMPLO É:
        # numeros[0].append(valor)
        # VOU ADICIONAR O VALOR NA CHAVE 0
    else:
        impares.append(valor)
        numeros.append(valor)
        impares.sort()
        numeros.sort()
        # NESSE CASO:
        # numeros[1].append(valor)
# NO CASO DO SORT
# numeros[0].sort()
# numeros[1].sort()
print('-=-' * 20)
print(f'Os valores pares foram {pares}')
# NO CASO DO PRINT
# print(f'Os valores pares foram: {numeros[0]}!')
print(f'Os valores impares foram {impares}')
# PRINT
# print(f'Os valores impares foram: {numeros[1]}')
print(f'Todos os valores são {numeros}')
