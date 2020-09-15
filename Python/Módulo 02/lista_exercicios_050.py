# DESAFIO 050
# ESTRUTURA FOR

# CRIE UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS
# MOSTRE A SOMA APENAS DOS QUE FOREM PARES
# SE O VALOR DIGITADOR FOR IMPAR, IGNORE-O

soma_pares = 0
cont_nume = 0
cont_nume_pares = 0
for c in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(c)))
    cont_nume += 1
    if numero % 2 == 0:
        soma_pares += numero
        cont_nume_pares += 1
print('Você informou {} números, {} são pares e a soma dos pares é {}'.format(cont_nume, cont_nume_pares, soma_pares))
print('FIM DO PROGRAMA')
