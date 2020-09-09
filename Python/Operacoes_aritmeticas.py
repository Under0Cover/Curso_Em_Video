# OPERAÇÕES ARITMÉTICAS

""" +   -> ADIÇÃO
    -   -> SUBTRAÇÃO
    *   -> MULTIPLICAÇÃO
    /   -> DIVISÃO
    **  -> POTÊNCIA
    //  -> DIVISÃO INTEIRA
    %   -> RESTO DA DIVISÃO

    OBS:
    =   -> RECEBE
    ==  -> IGUAL

    EXEMPLOS:
    ADIÇÃO              5 +  2 = 7
    SUBTRAÇÃO           5 -  2 = 3
    MULTIPLICAÇÃO       5 *  2 = 10
    DIVISÃO             5 /  2 = 2.5
    POTÊNCIA            5 ** 2 = 25     --> PODE SER USADA A FUNÇÃO DE POTÊNCIA --> pow(x, y)
    DIVISÃO INTEIRA     5 // 2 = 2
    RESTO DA DIVISÃO    5 %  2 = 1

    ORDEM DE PRECEDÊNCIA
    PARENTÊSES
    POTÊNCIA
    DIVISÃO, MULTIPLICAÇÃO, DIVISÃO INTEIRA E RESTO DA DIVISÃO [NA ORDEM QUE APARECER]
    SUBTRAÇÃO E ADIÇÃO [NA ORDEM QUE APARECER]"""

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
exponenciacao = numero1 ** numero2
print('A soma entre {} e {} é {}'.format(numero1, numero2, soma))
print('A subtração entre {} e {} é {}'.format(numero1, numero2, subtracao))
print('A multiplicação entre {} e {} é {}'.format(numero1, numero2, multiplicacao))
print('A divisão entre {} e {} é {:.3f}'.format(numero1, numero2, divisao)) #{:.3f} --> com 3 casas flutuantes
print('A divisão inteira entre {} e {} é {}'.format(numero1, numero2, divisao_inteira))
print('A exponênciação entre {} e {} é {}'.format(numero2, numero1, exponenciacao))
# print('A soma vales {}'.format(numero1+numero2))
# A forma do FORMAT(SOMA) só é usada quando não tem validade posterior do valor da soma
# Se for pra ser usada depois, tem que ser criada uma variável
# Para quebrar a linha \n
# Para não quebrar a linha end=' '