# DESAFIO 013
# DAR UM AUMENTO DE 15% DE SALÁRIO

salario = float(input('Digite o seu salário: '))
aumento = (salario + (salario * 0.15))
print('Seu salário antigo é de R$ {}, seu novo salário é de R$ {:.2f}'.format(salario, aumento))
# OUTRA FORMA DE FAZER:
# (SALARIO * 15 / 100) + SALARIO
