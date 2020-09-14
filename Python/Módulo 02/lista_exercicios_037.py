# DESAFIO 037
# ESTRUTURA IF-ELSE-ELIF

# CRIAR UM PROGRAMA QUE RECEBA UM NÚMERO
# E DÊ AS OPÇÕES DE CONVERSÕES:
# BINÁRIO
# OCTAL
# HEXADECIMAL

print('Conversão de números inteiros')
numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('( 1 ) - Conversão para BINÁRIO')
print('( 2 ) - Conversão para OCTAL')
print('( 3 ) - Conversão para HEXADECIMAL')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    print('O número {} convertido para Binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para Octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')
