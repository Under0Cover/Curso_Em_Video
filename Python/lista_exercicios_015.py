# DESAFIO 015
# ALUGUEL DE CARROS

dias = int(input('Quantos dias o carro ficou alugado?  '))
km = float(input('Quantos KM foram rodados?  '))
valor_dias = 60 * dias
valor_km = 0.15 * km
total = valor_dias + valor_km
print('O valor a pagar é R$ {:.2f} por dia e R$ {:.2f} por KM rodado, com um total de R$ {:.2f}'
      .format(valor_dias, valor_km, total))
