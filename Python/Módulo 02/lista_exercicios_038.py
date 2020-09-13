# DESAFIO 038
# ESTRUTURA IF-ELSE-ELIF

# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS
# RETORNE:
# SE O PRIMEIRO VALOR É MAIOR
# SE O SEGUNDO VALOR É MAIOR
# OU SE SÃO IGUAIS

valor1 = int(input('Escreva o primeiro valor: '))
valor2 = int(input('Escreva o segundo valor: '))
if valor1 > valor2:
    print('O {} é maior que o {}!'.format(valor1, valor2))
elif valor2 > valor1:
    print('O {} é maior que o {}!'.format(valor2, valor1))
else:
    print('Ambos são valores iguais')