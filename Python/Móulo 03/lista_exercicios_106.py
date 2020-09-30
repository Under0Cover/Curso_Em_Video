# DESAFIO 106
# ESTRUTURA FUNÇÃO 02

# FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON
# O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER
# QUANDO O USUÁRIO DIGITAR A PALAVRA 'FIM' O PROGRAMA SE ENCERRARÁ
# OBS: USE CORES

# IMPORTAÇÕES
from time import sleep

# CORES
cores = ('\033[m',              # 0 - SEM CORES
         '\033[0;30;41m',       # 1 - VERMELHO
         '\033[0;30;42m',       # 2 - VERDE
         '\033[0;30;43m',       # 3 - AMARELO
         '\033[0;30;44m',       # 4 - AZUL
         '\033[0;30;45m',       # 5 - ROXO
         '\033[7;30m',          # 6 - BRANCO
         )


# FUNÇÕES
def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 5)
    print(cores[6])
    help(comando)
    print(cores[0])
    sleep(2)


def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(1)


# PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA OLIVER_HELP', 4)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
