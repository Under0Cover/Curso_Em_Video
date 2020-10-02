# DESAFIO 108
# ESTRUTURA MÓDULOS

# ADAPTE O CÓDIGO DO DESAFIO 107
# CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA()
# QUE CONSIGA MOSTRAR OS VALORES COMO UM VALOR MONETÁRIO FORMATADO

# IMPORTAÇÕES
from modulos_exercicios import moeda

# PROGRAMA PRINCIPAL
numero = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(numero)} é {moeda.moeda(moeda.metade(numero))}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}')
print(f'Aumentando 10% de {moeda.moeda(numero)}, temos: {moeda.moeda(moeda.aumentar(numero))}')
print(f'Diminuindo 15% de {moeda.moeda(numero)}, temos: {moeda.moeda(moeda.diminuir(numero))}')

