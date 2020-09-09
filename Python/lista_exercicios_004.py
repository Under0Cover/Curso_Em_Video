# DESAFIO 004
""" DISSECANDO UMA VARIÁVEL """

print('Digite algo e o programa retornará verdadeiro ou falso para as afirmações...')
n = input('Digite algo:  ')
print(' ')
# type() --> Mostrar o tipo primitivo da variável
print('{} é do tipo primitivo: '.format(n), type(n))
print('Esse tipo de variável sempre vai retornar String')
print('Trolei... ')
print('rsrsrsrs')
print('Agora vai começar de verdade...')
print(' ')
# .isnumeric() --> É númerico?
print('{} é númerico?'.format(n), n.isnumeric())
# .isalpha() --> É letra?
print('{} é uma letra?'.format(n), n.isalpha())
# .isalnum() --> É alfanumérico?
print('{} é Alfanumérico?'.format(n), n.isalnum())
# .isupper() --> É tudo em maiuscúlas?
print('{} foi digitado em maiuscúlas?'.format(n), n.isupper())
# .islower() --> É tudo minuscúlas?
print('{} foi digitado em minuscúlas?'.format(n), n.islower())
# .isprintable --> É impresso?
print('{} pode ser impresso?'.format(n), n.isprintable())
# .isspace --> É um espaço?
print('{} é um espaço?'.format(n), n.isspace())
# .istitle() --> Letra maiuscúla?
print('{} começa com letra maiuscúla?'.format(n), n.istitle())
# Todos os exemplos usados pelo professor