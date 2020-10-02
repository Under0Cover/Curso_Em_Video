# DESAFIO 114
# TRATAMENTO DE ERROS

# CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM
# ESTÁ ACESSÍVEL PELO COMPUTADOR USADO

# IMPORTAÇÕES
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('O site Pudim está acessível no momento!')
    print(site.read())
