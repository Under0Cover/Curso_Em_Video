# DESAFIO 006
# IMPRIMIR O DOBRO, O TRIPLO E A RAIZ QUADRADA

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2) # --> raiz quadrada ou elevado a meio
print('O seu número {}, tem o dobro {}, o triplo {} e a raiz {:.2f}'.format(numero, dobro, triplo, raiz))
