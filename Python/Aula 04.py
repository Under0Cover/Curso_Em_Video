Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Olá, mundo!')
Olá, mundo!
>>> print('Estou começando a aprender Python')
Estou começando a aprender Python
>>> print(7+4)
11
>>> print('7'+'4')
74
>>> 7+4
11
>>> '7' + '4'
'74'
>>> print('Olá' + 5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('Olá' + 5)
TypeError: can only concatenate str (not "int") to str
>>> print('Olá' , 5)
Olá 5
>>> nome = 'Guanabara'
>>> idade = 25
>>> peso = 75.8
>>> print(nome, idade, peso)
Guanabara 25 75.8
>>> print(nome + idade + peso)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(nome + idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome?Tales Oliver
>>> nome = input ('Qual é a sua idade?')
Qual é a sua idade?36 anos
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome?Tales Oliver
>>> idade = input ('Qual é a sua idade?')
Qual é a sua idade?36 anos
>>> peso = input ('Quanto você pesa?')
Quanto você pesa?99.800 Kg
>>> print(nome, idade, peso)
Tales Oliver 36 anos 99.800 Kg
>>> 