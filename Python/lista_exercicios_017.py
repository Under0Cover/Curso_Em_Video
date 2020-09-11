# DESAFIO 017
# CÁLCULO DA HIPOTENUSA
# O EXERCÍCIO PROPOSTO É FAZER A CONTA DO TEOREMA DE PITAGORAS
# OBVIAMENTE QUE O PROFESSOR QUER QUE EU USE ALGO DA BIBLIOTECA MATH
# MAS, PRA GARANTIR A RESOLUÇÃO DO EXERCÍCIOS, EU VOU FAZER A CONTA NA BASE DA FÓRMULA

from math import sqrt
cat_adj = float(input('Digite o valor do Cateto Adjacente: '))
cat_op = float(input('Digite o valor do Cateto Oposto: '))
soma_catetos = ((cat_op ** 2) + (cat_adj ** 2))
hip = sqrt(soma_catetos)
print('O valor da hipotenusa é {:.2f}'.format(hip))

''' RESOLUÇÃO DO PROFESSOR

from math import hypot
cat_opo = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjascente: '))
hipoten = hypot(cat_opo, cat_adj)
print('A hipotenusa vai medir {:.2f}'.format(hipoten))'''