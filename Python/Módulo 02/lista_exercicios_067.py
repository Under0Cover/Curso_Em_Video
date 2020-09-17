# DESAFIO 067
# ESTRUTURA WHILE COM BREAK

# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO FOR NEGATIVO


while True:
    numero = int(input('Digite um número para ser calculado na tabuada: '))
    if numero < 0:
        print('PROGRAMA TABUADA ENCERRADO!!!')
        print('VOLTE SEMPRE')
        print('-=-' * 20)
        break
    print('-=-' * 20)
    for contador in range(1, 11):
        print(f'{numero} X {contador:2} = {numero * contador}')
    print('-=-' * 20)
