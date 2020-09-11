# DESAFIO 018
# DETERMINANDO SENO, COSSENO E TANGENTE DE UM ÂNGULO

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
# seno = math.sin           --> cálculo do seno (que pede em radianos)
# math.radians(angulo)      --> transformando os graus de celsius em radianos
cosseno = math.cos(math.radians(angulo))
# FAZENDO EXATAMENTE A MESMA COISA:
# USANDO A FUNÇÃO MATEMÁTICA DO COSSENO, PÓREM ELA RECEBE EM RADIANOS
# MATH.RADIANS CONVERTE OS GRAUS CELSIUS PARA RADIANOS
tangente = math.tan(math.radians(angulo))
# ESSA VOCÊ JÁ ENTENDEU :P
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
