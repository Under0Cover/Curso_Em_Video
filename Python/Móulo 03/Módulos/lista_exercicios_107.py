# DESAFIO 107
# ESTRUTURA MÓDULOS

# CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHAS AS FUNÇÕES
# -> AUMENTAR()
# -> DIMINUIR()
# -> DOBRO()
# -> METADE()

# FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULOS
# E USE ALGUMAS DESSAS FUNÇÕES
# IMPORTAÇÕES

from modulos_exercicios import moeda

# PROGRAMA PRINCIPAL
numero = float(input('Digite o preço R$:  '))
print(f'Aumentar 10% sobre o {numero} é {moeda.aumentar(numero)}!')
print(f'Diminuir 15% sobre o {numero} é {moeda.diminuir(numero)}!')
print(f'O dobro de {numero} é {moeda.dobro(numero)}!')
print(f'A metade de {numero} é {moeda.metade(numero)}!')

