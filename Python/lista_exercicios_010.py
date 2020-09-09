#DESAFIO 010
# CONVERSÃO DE REIAS PARA DOLARES

reais = float(input('Digite quantos reais você tem, e veremos quantos dolares você pode comprar: '))
# COTAÇÃO DO DOLAR NO DIA 09/09/20 -> R$ 5,36
dolar = (reais/5.36)
print('Com R$ {:.2f}, você pode ter US${:.2f}'.format(reais, dolar))
