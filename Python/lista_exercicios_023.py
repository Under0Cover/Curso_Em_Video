# DESAFIO 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGÍTIOS SEPRADOS

numero = int(input('Digite um número de 0 a 9999: '))
# AINDA NÃO DÁ PRA FAZER TRANSFORMANDO O NÚMERO NUMA STRING
# RESOLVER NA BASE DA MATEMÁTICA BRUTA MESMO
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
