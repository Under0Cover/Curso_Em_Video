# DESAFIO 099
# ESTRUTURA FUNÇÕES

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR()
# QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS
# SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR

# IMPORTAÇÕES
from time import sleep


# FUNÇÕES
def maior(*numeros):
    sleep(2)
    contador = maior = 0
    print('\nAnalisando os valores informados!')
    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.4)
        if contador == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        contador += 1
    print(f'\nForam informados {contador} valores ao todo!')
    print(f'O maior valor informado foi {maior}!')
    print('-' * 40)


# PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
