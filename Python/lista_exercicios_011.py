# DESAFIO 011
# DADO UMA LARGURA E UMA ALTURA, CALCULE A ÁREA DA PAREDE E A TINTA NECESSÁRIA PARA PINTA-LÁ
# CONSIDERANDO QUE CADA LITRO DE TINTA PINTE 2m²

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
metros = (largura*altura)
tinta = (metros/2)
print('Sendo a altura {:.2f} e a largura {:.2f}, sua parede tem {:.2f}m² e '
      'precisará de {:.2f} litros de tinta'.format(altura, largura, metros, tinta))
