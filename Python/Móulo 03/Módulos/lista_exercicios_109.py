# DESAFIO 109
# ESTRUTURA MÓDULO

# MODIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107
# PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS
# INFORMANDO SE O VALOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO
# PELA FUNÇÃO MOEDA() DESENVOLVIDA NO DESAFIO 108

# IMPORTAÇÕES
from modulos_exercicios import moeda_formatado

# PROGRAMA PRINCIPAL
numero = float(input('Digite o preço: '))
print(f'A metade de {moeda_formatado.moeda(numero)} é {moeda_formatado.metade(numero, True)}')
print(f'O dobro de {moeda_formatado.moeda(numero)} é {moeda_formatado.dobro(numero)}')
print(f'Aumentando 10% de {moeda_formatado.moeda(numero)}, temos: {moeda_formatado.aumentar(numero, True)}')
print(f'Diminuindo 15% de {moeda_formatado.moeda(numero)}, temos: {moeda_formatado.diminuir(numero)}')
# ALGUNS PRINTS ESTÃO COM A FORMATAÇÃO "TRUE" OUTROS SEM
# PARA EXEMPLIFICAR QUE NO MÓDULO A FORMATAÇÃO ESTÁ DEFINIDA COMO TRUE
