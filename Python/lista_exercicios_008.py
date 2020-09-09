# DESAFIO 008
# TRABALHANDO COM METRAGENS

# RECEBER UM VALOR EM METROS E IMPRIMIR EM CENTÍMETROS E MILÍMETROS

print('Informe um valor em metros e receba os centímetros e milímetros desse valor')
numero = float(input('Informe um valor: '))
cm = numero * 100
mm = numero * 1000
print('O seu valor {:.2f}m, tem {:.0f}cm e {:.0f}mm'.format(numero, cm, mm))
