# DESAFIO 104
# ESTRUTURA FUNÇÃO 02

# FAÇA UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT()
# QUE VAI FUNCIONAR DE FORMA SEMELHANTE À FUNÇÃO INPUT() DO PYTHON
# SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO


# FUNÇÕES
def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')