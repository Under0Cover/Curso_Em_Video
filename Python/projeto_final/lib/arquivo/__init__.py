# IMPORTAÇÕES
from projeto_final.lib.interface import *

# FUNÇÕES


# VERIFICAR EXISTENCIA ARQUIVO
def arquivo_existe(nome):
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


# CRIAR ARQUIVO
def criar_arquivo(nome):
    try:
        criar = open(nome, 'wt+')
        criar.close()
    except:
        print('\033[0;31mHouve um ERRO na criação do arquivo!!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# LER ARQUIVO
def ler_arquivo(nome):
    try:
        abrir = open(nome, 'rt')
    except:
        print('\033[0;31mERRO ao ler o arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        abrir.close()



# CADASTRAR PESSOAS
def cadastrar_pessoas(arquivo, nome='desconhecido', idade=0):
    try:
        abrir = open(arquivo, 'at')
    except:
        print('\033[0;31mHouve um ERRO na abertura do arquivo!')
    else:
        try:
            abrir.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mHouve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            abrir.close()
