# DESAFIO 048
# ESTRUTURA FOR

# FAÇA UM PROGRAMA QUE CALCULE A SOMA
# ENTRE TODOS OS NÚMEROS
# IMPARES E MÚLTIPLIS DE 3
# NO INTERVALO DE 1 ATÉ 500

numeros_aceitos = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        numeros_aceitos += c
print(numeros_aceitos)
print('FIM DO PROGRAMA')
