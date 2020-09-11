# DESAFIO 034
# AUMENTO DE SALÁRIOS

# CRIE UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO
# SE ELE GANHAR ACIMA DE R$ 1.250,00 O AUMENTO É DE 10%
# SE ELE GANHAR ABAIXO DE R$ 1.250,00 O AUMENTO É DE 15%

salario = float(input('Digite o seu salário para saber o aumento: '))
if salario > 1250:
    aumento = (salario + (salario * 0.1))
    print('O seu salário receberá um aumento de 10%, passando a ser R$ {:.2f}'.format(aumento))
else:
    aumento = (salario + (salario * 0.15))
    print('O seu salário receberá um aumento de 15%, passando a ser RR$ {:.2f}'.format(aumento))
