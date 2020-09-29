# DESAFIO 098
# ESTRUTURA FUNÇÕES

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR()
# QUE RECEBA TRÊS PARÂMETROS: INICIO, FIM E PASSO E REALIZA A CONTAGEM
# SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA
# A) DE 1 ATÉ 10, DE 1 EM 1
# B) DE 10 ATÉ 0, DE 2 EM 2
# C) UMA CONTAGEM PERSONALIZADA

from time import sleep
# FUNÇÃO CONTADOR
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    sleep(2.5)
    if inicio < fim:
        contagem = inicio
        while contagem <= fim:
            print(f'{contagem} ', end='')   # flush=True
            # O PROFESSOR TEVE PROBLEMAS NA UTILIZAÇÃO DO SLEEP 0.5
            # E PRA ISSO UTILIZOU O FLUSH = TRUE
            # NA EXECUÇÃO DO MEU PROGRAMA NÃO HOUVE ESSE PROBLEMA
            sleep(0.5)
            contagem += passo
        print('FIM!')
    else:
        contagem = inicio
        while contagem >= fim:
            print(f'{contagem} ', end='')   # flush=True
            sleep(0.5)
            contagem -= passo
        print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
