# DESAFIO 035
# TRÊS RETAS

# ESCREVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA SE ELAS PODEM FORMAR UM TRIÂNGULO

from time import sleep
lado1 = float(input('Digite a medida de um lado do Triângulo: '))
lado2 = float(input('Digite a medida de outro lado do Triângulo: '))
lado3 = float(input('Digite a medida do última lado do Triângulo: '))
print('Calculando....')
sleep(3)
if lado1 < (lado2 + lado3) and lado2 < (lado3 + lado1) and lado3 < (lado1 + lado2):
    print('Essas medidas PODEM formar um Triângulo')
else:
    print('Essas medidas NÃO PODEM formar um Triângulo')