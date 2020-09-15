# DESAFIO 046
# ESTRUTURA FOR

# FAÇA UM PROGRAMA QUE MOSTRE A CONTAGEM REGRESSIVA
# INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FOGOS')
