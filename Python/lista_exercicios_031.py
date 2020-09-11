# DESAFIO 031
# VIAGEM POR KM

# CRIE UM PROGRAMA QUE PERGUNTA A DISTÂNCIA DA VIAGEM POR KM
# VIAGENS ATÉ 200KM, COBRAR R$ 0.50 POR KM
# VIAGENS COM MAIS DE 200KM, COBRAR R$ 0.45 POR KM

distancia = float(input('Digite a distância da viagem que você quer fazer: '))
if distancia <= 200:
    valor = (distancia * 0.50)
    print('O valor da viagem é de {:.2f}'.format(valor))
else:
    valor = (distancia * 0.45)
    print('O valor da viagem é de {:.2f}'.format(valor))
