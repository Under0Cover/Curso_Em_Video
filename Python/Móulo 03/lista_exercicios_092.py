# DESAFIO 092
# ESTRUTURA DICIONÁRIO

# CRIE UM PROGRAMA QUE LEIA O NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO
# CADASTRE (COM A IDADE) EM UM DICIONÁRIO
# SE A CARTEIRA DE TRABALHO FOR DIFERENTE DE ZERO
# O DICIONÁRIO RECEBERÁ TAMBÉM:
# ANO DE CONTRATAÇÃO E O SALÁRIO
# CALCULE E ACRESCENTE ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA IRÁ SE APOSENTAR

from datetime import  datetime
dados_trabalhador = dict()
dados_trabalhador['Nome'] = str(input('Digite o nome do trabalhador: '))
ano_nascimento = int(input('Digite o ano de nascimento do trabalhador: '))
dados_trabalhador['Idade'] = datetime.now().year - ano_nascimento
dados_trabalhador['Ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if dados_trabalhador['Ctps'] != 0:
    dados_trabalhador['Contrato'] = int(input('Ano de contratação: '))
    dados_trabalhador['Salario'] = float(input('Salário (em R$): '))
    dados_trabalhador['Aposentadoria'] = (dados_trabalhador['Contrato'] + 35) - ano_nascimento
print('-=' * 20)
for chaves, valores in dados_trabalhador.items():
    print(f'-> {chaves} tem o valor {valores}.')
