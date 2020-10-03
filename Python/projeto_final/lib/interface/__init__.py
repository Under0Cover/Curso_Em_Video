# FUNÇÕES

# LINHA DE DIVISÃO
def linha(tamanho = 42):
    return '-' * tamanho



# LEIA INTEIRO
def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return numero



# CABEÇALHO
def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())



# MENU
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[34m{contador} - {item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('Sua Opção:\033[0;31m  \033[m')
    return opcao

