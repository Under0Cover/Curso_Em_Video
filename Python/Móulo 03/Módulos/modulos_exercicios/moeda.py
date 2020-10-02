# FUNÇÕES DOS EXERCÍCIOS

def aumentar(numero):
    """
    -> Função para aumentar 10% o valor do número
    :param numero: Número a ser calculado
    :return: Retorna o número com 10% de acréscimo
    By: Tales Oliver
    """
    operacao = numero + (numero * 0.10 )
    return operacao


def diminuir(numero):
    """
    -> Função para descontar 15% o valor do número
    :param numero: Número a ser calculado
    :return: Retorna o número com 15% de desconto
    By Tales Oliver
    """
    operacao = numero - (numero * 0.15 )
    return operacao


def dobro(numero):
    """
    -> Função para calcular o dobro de um número
    :param numero: Número a ser calculado
    :return: Retorna o dobro do número
    By Tales Oliver
    """
    operacao = numero * 2
    return operacao



def metade(numero):
    """
    -> Função para calcular a metade de um número
    :param numero: Número a ser calculado
    :return: Retorna a metade do número
    By: Tales Oliver
    """
    operacao = numero / 2
    return operacao

def moeda(numero):
    """
    -> Função para formatar os prints de forma monetária
    :param numero: Número a ser formatado
    :return: Retorna a impressão com formatação monetária
    By Tales Oliver
    """
    return f'R$ {numero:.2f}'
