# FUNÇÕES DE VALIDAÇÃO

def leiaDinheiro(mensagem):
    """
    -> Função de validação de números
    :param mensagem: Conferir a mensagem para ter certeza que é número
    :return: Retorna um float
    By Tales Oliver
    """
    ok = False
    while True:
        numero = str(input(mensagem)).replace(',', '.')
        if numero.isalpha() or numero.strip() == '':
            print('\033[0;31mERRO! Digite um número válido.')
            print(f'{numero} não é um número válido\033[m')
        else:
            ok = True
            return float(numero)
