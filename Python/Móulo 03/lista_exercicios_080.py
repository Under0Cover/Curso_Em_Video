# DESAFIO 080
# ESTRUTURA LISTA

# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES
# E CADASTRE ELES EM UMA LISTA
# INSERIDOS NA POSIÇÃO CORRETA DE ORDEM CRESCENTE
# SEM USAR O COMANDO SORT()
# NO FINAL MOSTRE A LISTA ORDENADA NA TELA

numero = []
for contador in range(0, 5):
    aprovacao = int(input(f'Digite o valor da posição {contador}: '))
    if contador == 0 or aprovacao > numero[-1]:
        # SE FOR O PRIMEIRO NÚMERO PODE ADICIONAR SEM PROBLEMAS
        # SE O NÚMERO (APROVACAO) FOR MAIOR QUE O ÚLTIMO, TAMBÉM PODE ADICIONAR SEM PROBLEMAS
        numero.append(aprovacao)
        print('Adicionado ao final da Lista!')
    elif aprovacao in numero:
        # SE FOR UM NÚMERO REPETIDO NÃO PODE ADICIONAR
        print('Número já digitado.')
    else:
        posicao = 0
        while posicao < len(numero):
            # ENQUANTO A POSIÇÃO FOR MENOR QUE O TAMANHO DA LISTA
            if aprovacao < numero[posicao]:
                # SE O NÚMERO (APROVACAO) FOR MENOR QUE O NÚMERO DA POSIÇÃO
                numero.insert(posicao, aprovacao)
                # EU VOU INSERIR NA POSICAO O NÚMERO (APROVACAO)
                print(f'Adicionado na posição {posicao} da Lista!')
                break
            posicao += 1
print('-=-' * 20)
print(f'Os valores digitados em ordem foram {numero}')
