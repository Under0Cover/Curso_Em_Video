# DESAFIO 083
# ESTRUTURA LISTA

# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUE USE PARÊNTESES
# SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM PARÊNTESES ABERTOS E FECHADOS CORRETAMENTE

expressao = str(input('Digite a expressão: '))
# TODA STRING É UMA LISTA E POR ISSO PODE SER DIVIDIDA
# EU CONSIGO UTILIZAR O FOR PARA PEGAR CADA LETRA OU CARACTER
pilha = []
for simbolo in expressao:
    # EU VOU VERIFICAR SE ELE É UM PARÊNTESE ABRINDO OU FECHANDO
    if simbolo == '(':
        pilha.append('(')
        # CADA VEZ QUE EU ENCONTRAR UM PARÊNTESE NA EXPRESSAO, EU ADICIONO A PILHA
    elif simbolo == ')':
        if len(pilha) > 0:
            # SE A PILHA FOR MAIOR QUE ZERO, QUER DIZER QUE EXISTEM PARÊNTESES ABERTOS
            pilha.pop()
            # EU VOU REMOVER O ÚLTIMO ELEMENTO
        else:
            # SE A PILHA ESTÁ VAZIA, SIGNIFICA QUE TEM UM PARÊNTESE FALTANDO
            pilha.append(')')
            break
if len(pilha) == 0:
    # QUER DIZER QUE A QUANTIDADE DE PARÊNTESE ESTÁ CORRETA
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')