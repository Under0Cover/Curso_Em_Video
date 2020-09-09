# TIPOS PRIMITIVOS
# ni = input('Digite um número: ')
# n2 = input('Digite outro número: ')

"""s = n1 + n2
O MAIS NESSE CASO NÃO REPRESENTA SOMA, REPRESENTA CONTATENAÇÃO
TODO VALOR DIGITADO NO INPUT É CONSIDERADO UMA STRING, NÃO UM NÚMERO
UTILIZA-SE O *INT* (TIPO PRIMITIVO) PARA RECEBER UM INTEIRO"""

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
# print('A soma dos números é ', soma)
# PODE-SE MOSTRAR O TIPO DA CLASSE USANDO => print(type(variavel))

"""OS TIPOS PRIMITIVOS MAIS BÁSICO DO PYTHON SÃO:
A) INT - TIPO INTEIRO ==> EXEMPLOS: 7 -4 0 9875
B) FLOAT - NÚMEROS VARIÁVEIS (NÚMEROS REAIS) ==> EXEMPLOS: 4.5 0.076 15.223
C) BOOL - BOOLEANOS (VERDADEIRO OU FALSO) ==> EXEMPLOS: TRUE FALSE *USAR SEMPRE A PRIMEIRA LETRA NA MAISCÚLA
D) STR - TIPO STRINGS OU CARACTERES ==> 'Olá' '7.5' ' ' *STRING VAZIA"""

"""O PRINT USADO COM CHAVES {} (MASCARA) QUE SERÁ SUBSTITUÍDA POR UM MÉTODO DA PRÓPRIA STRING
ESSE MODELO DE USAR O PRINT É MAIS RECENTE NO PYTHON 3"""

# print('A soma entre ', numero1, ' e ', numero2, ' é ', soma)
print('A soma entre {} e {} vale {}'.format(numero1, numero2, soma))

