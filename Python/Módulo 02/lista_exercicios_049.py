# DESAFIO 049
# ESTRUTURA FOR

# REFAÇA O DESAFIO 009
# DESAFIO 009 É A TABUADA
# UTILIZANDO O LAÇO FOR

numero = int(input('Digite um número para cálculo da tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(numero, c, (c * numero)))
print('FIM DO PROGRAMA')
