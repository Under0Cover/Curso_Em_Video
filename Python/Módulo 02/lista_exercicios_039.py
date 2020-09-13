# DESAFIO 039
# ESTRUTURA IF-ELIF-ELSE

# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
# E DÊ INFORMAÇÕES SOBRE O ALISTAMENTO MILITAR

from datetime import date
ano_sistema = date.today().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_sistema - ano_nascimento
if idade == 17 or idade == 18:
    print('Você está em idade militar!')
    print('Vá até a junta militar da sua cidade obter informações')
elif idade < 17:
    print('A sua idade militar ainda não chegou')
    falta_anos = 18 - idade
    print('Falta(m) {} ano(s) para o seu alistamento'.format(falta_anos))
else:
    print('A sua hora de apresentar-se à junta militar já passou')
    sobra_anos = idade - 18
    print('Você está atrasado há {} ano(s)'.format(sobra_anos))

