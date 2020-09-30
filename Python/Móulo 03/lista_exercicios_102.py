# DESAFIO 102
# ESTRUTURA FUNÇÕES 02

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL()
# QUE RECEBA DOIS PARÂMETROS:
# O PRIMEIRO INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW
# QUE SERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO FATORIAL

# FUNÇÕES
def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :param numero: Número a ser calculado
    :param show: (Opcional) Mostrar toda a conta
    :return: O resultado da conta fatorial
    """
    fator = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fator *= contador
    return fator


# PROGRAMA PRINCIPAL
print(fatorial(5))