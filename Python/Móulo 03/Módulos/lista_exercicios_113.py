# DESAFIO 113
# TRATAMENTO DE ERROS E EXCEÇÕES

# REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104
# INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE UM NÚMERO DE TIPO INVÁLIDO
# APROVEITE E CRIE TAMBÉM A FUNÇÃO LEIAFLOAT() COM A MESMA FUNCIONALIDADE

# FUNÇÕES
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


def leiaReal(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return numero

# PROGRAMA PRINCIPAL
numero_inteiro = leiaInt('Digite um número INTEIRO: ')
numero_real = leiaReal('Digite um número REAL: ')
print(f'Você acabou de digitar o número inteiro: {numero_inteiro} e o número real: {numero_real}!')
