# DESAFIO 043
# ESTRUTURA IF-ELIF-ELSE

# CÁLCULO DE IMC
# 5 RETORNOS
# < 18.5 ABAIXO DO PESO
# ENTRE 18.5 E 25 PESO IDEAL
# 25 A 30: SOBREPESO
# 30 A 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MÓRBIDA

from math import pow
from time import sleep
print('Vamos fazer o cálculo do IMC?')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = float(peso / pow(altura, 2))
print('O cálculo do seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso ideal!')
elif imc < 30:
    print('Sobrepeso!')
elif imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
