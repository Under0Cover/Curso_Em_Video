""" APRENDENDO A USAR BIBLIOTECAS IMPORTADAS

BIBLIOTECA "MATH" DO PRÓPRIO PYTHON

ALGUMAS FUNCIONALIDADES DA BIBLIOTECA "MATH"
CEIL                        --> ARREDONDA UM NÚMERO PARA CIMA
FLOOR                       --> ARREDONDA UM NÚMERO PARA BAIXO
TRUNC                       --> TRUNCATE ELIMINA OS NÚMEROS PICADOS
POW                         --> POWER (POTÊNCIA)
SQRT                        --> RAIZ QUADRADA
FACTORIAL                   --> FATORIAL

IMPORT MATH                 --> IMPORTA TODA A BIBLIOTECA
FROM MATH IMPORT FUNÇÃO     --> IMPORTA APENAS A FUNÇÃO MENCIONADA
* PODE-SE IMPORTAR MAIS DE UMA FUNÇÃO, SEPARANDO ELAS POR VÍRGULA * """

import math
# from math import sqrt, floor
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
# raiz = sqrt(numero)
print('A raiz quadrada de {} é igual a {:.2f}'.format(numero, raiz))
# print('A raiz quadrada de {} é igual a {:.2f}'.format(num, floor(raiz)))
