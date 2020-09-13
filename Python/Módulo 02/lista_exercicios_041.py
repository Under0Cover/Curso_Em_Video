# DESAFIO 041
# ESTRUTURA IF-ELIF-ELSE

# CRIAR UM PROGRAMA QUE RECEBA O ANO DE NASCIMENTO E INFORME A CATEGORIA DE NATAÇÃO ADEQUADA
# RETORNO:
# 9 ANOS: MIRIM
# 14 ANOS: INFANTIL
# 19 ANOS: JUNIOR
# 20 ANOS: SÊNIOR
# ACIMA: MASTER

from datetime import date
ano_sistema = date.today().year
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_sistema - ano_nascimento
if idade < 9:
    print('Crianças até 9 anos fazem parte da categoria Mirim')
    print('Como a sua idade é de {}, essa é a sua categoria'.format(idade))
elif idade < 14:
    print('Crianças até 14 anos fazem parte da categoria Infantil')
    print('Como a sua idade é de {}, essa é a sua categoria'.format(idade))
elif idade < 19:
    print('Adolescentes até 19 anos fazem parte da categoria Júnior')
    print('Como a sua idade é de {}, essa é a sua categoria'.format(idade))
elif idade < 20:
    print('Adolescentes até 20 anos fazem parte da categoria Sênior')
    print('Como a sua idade é de {}, essa é a sua categoria'.format(idade))
else:
    print('Acima de 20 anos, a categoria é Master')
    print('Como a sua idade é de {}, essa é a sua categoria'.format(idade))
