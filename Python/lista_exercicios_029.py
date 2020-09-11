# DESAFIO 029
# RADAR

# CRIE UM PROGRAMA QUE LEIA A VELOCIDADE DO CARRO
# SE ELE ESTIVER ACIMA DE 80 KM/H, O CARRO DEVERÁ SER MULTADO
# R$ 7 PRA CADA KM/H ACIMA DO PERMITIDO

velocidade = float(input('Qual a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('VOCÊ ESTÁ ACIMA DA VELOCIDADE PERMITIDA!!!')
    print('Seu carro foi multado!!!!')
    print('O valor da multa é {:.2f}'.format(multa))
else:
    print('MUITO BEM!!!!')
    print('Respeitar o limite de velocidade é bom pro bolso')
    print('E salva vidas')
    print('Respeite a vida. Respeite o trânsito!')
