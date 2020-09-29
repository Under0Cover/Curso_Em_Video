# DESAFIO 096
# ESTRUTURA FUNÇÕES

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA AREA()
# ELA RECEBERÁ AS DIMENSÕES DE UM TERRENO RETANGULAR
# (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO

# FUNÇÃO ÁREA
def area(comprimento, largura):
    area = comprimento * largura
    print(f'O terrno tem {comprimento}m e {largura}m, sendo a área de {area}m²!')

# PROGRAMA PRINCIPAL
print('Metragem do terreno')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(comprimento, largura)
