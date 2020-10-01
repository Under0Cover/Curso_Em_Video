# FUNÇÕES
def fatorial(numero):
    fator = 1
    for contador in range(1, numero + 1):
        # AQUI A SOMA É UTILIZADA POR CONTA DAQUELE DETALHE DO RANGE NO PYTHON
        # O RANGE VAI ATÉ UM NÚMERO ANTES, COM A SOMA, OBRIGAMOS ELE A IR ATÉ O NÚMERO QUE DESEJAMOS
        fator *= contador
    return fator


def dobro(numero):
    return numero * 2


def triplo(numero):
    return numero * 3