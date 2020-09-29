# DESAFIO 097
# ESTRUTURA FUNÇÕES

# FAÇA UM PROGRAMA QUE TENHA UM FUNÇÃO CHAMADA ESCREVA()
# QUE RECEBA UM TEXTO COMO PARÂMETROS
# E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL

# FUNÇÃO ESCREVA
def escreva(mensagem):
    print('-' * len(mensagem))
    print(mensagem)
    print('-' * len(mensagem))


# PROGRAMA PRINCIPAL
mensagem = str(input('Digite a sua mensagem: '))
escreva(mensagem)