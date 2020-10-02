# FUNÇÕES

def aumentar(numero, aumento):
    """
    -> Função para calcular aumento de valores em porcentagem
    :param numero: Número a ser calculado
    :param aumento: Porcentagem a ser adicionada
    :return: Retorna o novo valor
    By Tales Oliver
    """
    operacao = numero + (numero * (aumento / 100))
    return operacao


def diminuir(numero, desconto):
    """
    -> Função para calcular desconto de valores em porcentagem
    :param numero: Número a ser calculaddo
    :param desconto: Porcentagem a ser descontada
    :return: Retorna o novo valor
    By Tales Oliver
    """
    operacao = numero - (numero * (desconto / 100))
    return operacao


def dobro(numero):
    """
    -> Função para calcular o dobro de um valor
    :param numero: Número a ser calculado
    :return: Retorna o dobro do número informado
    By Tales Oliver
    """
    operacao = numero * 2
    return operacao


def metade(numero):
    """
    -> Função para calcular a metade de um valor
    :param numero: Número a ser calculado
    :return: Retorna a metade do valor informado
    By Tales Oliver
    """
    operacao = numero / 2
    return operacao


def moeda(numero):
    """
    -> Função de formatação monetária
    :param numero: Número a ser formatado
    :return: Retorna o número original com formatalção monetária
    By Tales Oliver
    """
    return f'R$ {numero:.2f}'


def linha():
    """
    -> Função para adicionar "linha"
    :return: Retorna a impressão de 30 caracteres "menos"
    By Tales Oliver
    """
    print('-' * 30)


def resumo(numero, aumento, desconto):
    """
    -> Função que calcula o dobro, a metade, o acréscimo e o desconto
    de um mesmo número
    :param numero: Número a sofrer os calculos
    :param aumento: Porcentagem a ser acrescida
    :param desconto: Desconto a ser reduzido
    :return: Retorna um programa formatado, como um resumo
    Com o valor inicial, dobro do valor, metade do valor
    Além de acréscimo e desconto em porcentagem
    Também imprime linhas para melhor visualização
    By Tales Oliver
    """
    linha()
    print('Resumo do Valor'.center(30))
    linha()
    print(f'Preço analisado: \t{moeda(numero)}')
    print(f'Dobro do preço: \t{moeda(dobro(numero))}')
    print(f'Metade do preço: \t{moeda(metade(numero))}')
    print(f'{aumento}% de aumento: \t{moeda(aumentar(numero, aumento))}')
    print(f'{desconto}% de desconto: \t{moeda(diminuir(numero, desconto))}')
    linha()
