# DESAFIO 051
# ESTRUTURA FOR

# CRIE UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA
# NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DE PROGRESSÃO ARITMÉTICA

# RELEMBRANDO...
# PA É UMA SEQUÊNCIA DE SOMAS OU SUBTRAÇÕES
# PRIMEIRO TERMO É O INÍCIO
# RAZÃO É A SEQUÊNCIA

inicio = int(input('Digite o início da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
for c in range(1, 11):
    inicio += razao
    print(inicio)

# CONSEGUI FAZER NA SOMA

