# DESAFIO 110
# ESTRUTURA MÓDULOS

# ADICIONE AO MÓDULO MOEDA.PY CRIADO NOS DESAFIOS ANTERIORES
# UMA FUNÇÃO CHAMADA RESUMO()
# QUE MOSTRE NA TELA ALGUMAS INFORMAÇÕES GERADAS PELAS FUNÇÕES JÁ CRIADAS

#IMPORTAÇÕES
from modulos_exercicios import moeda_resumo

# PROGRAMA PRINCIPAL
numero = float(input('Digite o preço em R$: '))
moeda_resumo.resumo(numero, 80, 35)
