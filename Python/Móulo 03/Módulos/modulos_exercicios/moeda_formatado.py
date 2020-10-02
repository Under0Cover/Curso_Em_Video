# FUNÇÃO DOS EXERCÍCIOS

def aumentar(numero, formatado=True):
    """
    -> Função para aumentar em 10% o valor do número
    :param numero: Número a ser aumentando
    :param formatado: Formatação para moeda, com True ligado
    :return: Retorna o novo valor
    Bt Tales Oliver
    """
    operacao = numero + (numero * 0.10)
    if formatado:
        return f'R$ {operacao:.2f}'
    else:
        return operacao


def diminuir(numero, formatado=True):
    """
    -> Função para descontar 15% do número
    :param numero: Número a sofrer o desconto
    :param formatado: Formatação monetária
    :return: Retorna o novo valor
    By Tales Oliver
    """
    operacao = numero - (numero * 0.15)
    if formatado:
        return f'R$ {operacao:.2f}'
    else:
        return operacao


def dobro(numero, formatado=True):
    """
    -> Função para calcular o dobro
    :param numero: Número a sofrer o calculo
    :param formatado: Formatação monetária
    :return: Retorna novo valor
    By Tales Oliver
    """
    operacao = numero * 2
    if formatado:
        return f'R$ {operacao:.2f}'
    else:
        return operacao


def metade(numero, formatado=True):
    """
    -> Função para calculo da metade
    :param numero: Número a sofrer o calculo
    :param formatado: Formatação monetária
    :return: Retorna novo valor
    By Tales Oliver
    """
    operacao = numero / 2
    if formatado:
        return f'R$ {operacao:.2f}'
    else:
        return operacao


def moeda(numero):
    """
    -> Função para formatação monetária
    :param numero: Número a ser formatado
    :return: Retorna formatação monetária
    By Tales Oliver
    """
    return f'R$ {numero:.2f}'
