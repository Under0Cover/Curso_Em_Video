# FUNÇÕES 02

# -> INTERACTIVE HELP
# -> DOCSTRINGS
# -> ARGUMENTOS OPICIONAIS
# -> ESCOPO DE VARIÁVEIS
# -> RETORNO DE RESULTADOS

# --- TEORIA ---




# INTERACTIVE HELP
# AJUDA INTERATIVA

help(print)

print(input.__doc__)




# DOCSTRINGS
def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param inicio: Início da contagem
    :param fim: Fim da contagem
    :param passo: Passo da contagem
    :return: Sem retorno
    Função criada por Tales Oliver
    """
    numeros = inicio
    while numeros <= fim:
        print(f' {numeros}', end='..')
        numeros += passo
    print(' FIM!')

contador(2, 10, 2)

help(contador)




# ARGUMENTOS OPICIONAIS


def somar(a = 0, b = 0, c = 0):
    soma = a + b + c
    print(f'A soma vale {soma}')


somar(2, 3, 5)
somar(4, 8)
somar(1)
somar()




# ESCOPO DE VARIÁVEIS

# FUNÇÕES
# TESTE 01
def teste():
    x = 8
    print(f'Na função teste, n vale {n}!')
    print(f'Na função teste, x vale {x}!')
    # COMO O X ESTÁ DECLARADO DENTRO DA FUNÇÃO
    # A DECLARAÇÃO DE X É UMA DECLARAÇÃO LOCAL
    # OU SEJA, FORA DA FUNÇÃO TESTE ELA NÃO FUNCIONA


# PROGRAMA PRINCIPAL
n = 2
print(f'No programa principal, n vale {n}!')
teste()
# print(f'No programa principal, x vale {x}!')
# A DECLARAÇÃO DE N É UMA DECLARAÇÃO GLOBAL
# OU SEJA, ELA FUNCIONA EM TODO O PROGRAMA
# O MESMO NÃO ACONTECE COM X POR SER UMA DECLARAÇÃO LOCAL


# TESTE 02
def funcao():
    n1 = 4
    print(f'N1 LOCAL vale {n1}!')


n1 = 2
funcao()
print(f'N1 GLOBAL vale {n1}!')

# TESTE 03
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A LOCAL vale {a}!')
    print(f'B LOCAL vale {b}!')
    print(f'C LOCAL vale {c}!')


a = 5
teste(a)
print(f'A GLOBAL vale {a}')



# RETORNO DE VALORES
# TESTE 01
def somar(a = 0, b = 0, c = 0):
    soma = a + b + c
    print(f'A soma vale {soma}!')


somar(3, 2, 5)
somar(2, 2)
somar(3)


# TESTE 02
def somar(a = 0, b = 0, c = 0):
    soma = a + b + c
    return soma


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}!')


# --- PRÁTICA ---
# EXEMPLO 01
def fatorial(numero = 1):
    fator = 1
    for contador in range(numero, 0, -1):
        fator *= contador
    return fator

numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é igual a {fatorial(numero)}!')
fator1 = fatorial(5)
fator2 = fatorial(4)
fator3 = fatorial()
print(f'Os resultados são {fator1}, {fator2} e {fator3}!')


# EXEMPLO 02
def par_impar(numero = 0):
    if numero % 2 == 0:
        return True
    else:
        return False


numero = int(input('Digite um número: '))
if par_impar(numero):
    print('É par!')
else:
    print('Não é par')

