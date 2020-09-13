# DESAFIO 036
# ESTRUTURA IF-ELIF-ELSE

# PROGRAMA PARA APROVAR EMPRÉSTIMO BANCÁRIO PARA COMPRA DE CASAS

# VALOR DA CASA / QUANTOS ANOS = MENSALIDADE
# MENSALIDADE NÃO PODE SER MAIS QUE 30% SALÁRIO

from time import sleep
print('\033[31m-=-' * 40)
print('                                              -=-=- SIMULAÇÃO DE EMPRÉSTIMO -=-=-')
print('\033[31m-=-' * 40)
print(' ')
print(' ')
valor_casa = int(input('Digite o valor total da casa: '))
sleep(2)
duracao = int(input('Digite (em anos) o prazo do financiamento: '))
duracao_meses = duracao * 12
sleep(2)
print(' ')
print(' ')
salario = float(input('Digite a média salarial da família: '))
sleep(1)
mensalidade = valor_casa / duracao_meses
print('Os bancos não aprovam financiamento mais altos que 30% da soma dos Salários')
print('A casa que você quer comprar, por mês custa: R$ {:.2f}'.format(mensalidade))
sleep(2)
if mensalidade < (salario * 0.3):
    print('O Banco tem o prazer de anunciar que seu crédito é suficiente para o financiamento!')
else:
    print('O Banco informa que sua análise de crédito contém riscos e não vamos autorizar o financiamento!')