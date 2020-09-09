# DESAFIO 012
# DESCONTO EM PORCENTAGEM

preco = float(input('Digite o preço original: '))
desconto = (preco-(preco*0.05))
# 0.05 é o desconto de 5%
print('Com 5% de desconto, o preço de {}, passa a ser {}, à vista'.format(preco, desconto))
# OUTRA FORMA DE FAZER A PORCENTAGEM É:
# PRECO * DESCONTO / 100