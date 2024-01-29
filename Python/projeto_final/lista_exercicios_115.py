# DESAFIO 115
# TRATAMENTO DE ERROS

# CRIE UM PEQUENO SISTEMA MODULARIZADO
# QUE PERMITE CADASTRAR PESSOAS PELO NOME E IDADE
# EM UM ARQUIVO DE TEXTO SIMPLES
# O SISTEMA SÓ VAI TER 02 OPÇÕES:
# CADASTRAR UMA NOVA PESSOA
# E LISTAR TODAS AS PESSOAS CADASTRADAS

# IMPORTAÇÕES
from lib.interface import *
from lib.arquivo import *
from time import sleep

# ARQUIVO
arquivo = 'projeto_final_curso_em_video.txt'
if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)


# PROGRAMA PRINCIPAL
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # LER O ARQUIVO COM O CADASTRO DAS PESSOAS
        ler_arquivo(arquivo)
    elif resposta == 2:
        # CADASTRAR NOVAS PESSOAS NO ARQUIVO
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar_pessoas(arquivo, nome, idade)
    elif resposta == 3:
        # SAIR DO SISTEMA
        cabecalho('Saindo do Sistema...')
        sleep(0.8)
        cabecalho('Até logo!')
        sleep(1.5)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
