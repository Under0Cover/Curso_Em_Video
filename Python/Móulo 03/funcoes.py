# FUNÇÕES

# --- TEORIA ---

# USADO PARA COMANDOS REPETITIVOS E FUNÇÕES DE ROTINA
# DEF É A SIGLA DE DEFINIÇÃO
# DEFINIÇÃO DA FUNÇÃO

def mostraLinha():
    print('-' * 40)


def mensagem(mensagem):
    print('-' * 40)
    print(mensagem)
    print('-' * 40)


mostraLinha()
print(' SISTEMA DE ALUNOS ')
mostraLinha()
print(' CADASTRO DE FUNCIONÁRIOS ')
mostraLinha()
print(' ERRO DO SISTEMA ')
mostraLinha()

mensagem('SISTEMA DE PONTOS')
mensagem('CADASTRO DE LIVROS')
mensagem('ERRO DE LOGIN')

# --- PRÁTICA ---
# EXEMPLO DE ROTINA

# PROGRAMA PRINCIPAL
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)


# SIMPLIFICANDO A SOMA
def soma(a, b):
    s = a + b
    print(s)


# PROGRAMA PRINCIPAL
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=4, b=5)
soma(b=4, a=5)


# EMPACOTAMENTO DE FUNÇÃO
def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)



def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)