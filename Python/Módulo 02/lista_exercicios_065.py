# DESAFIO 065
# ESTRUTURA WHILE

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS
# NO FINAL, ELE DEVE MOSTRAR A MÉDIA ENTRE TODOS OS NÚMEROS
# QUAL É O MAIOR VALOR E QUAL É O MENOR VALOR
# DEPOIS DISSO O PROGRAMA DEVE PERGUNTAR SE O USUÁRIO QUER SAIR OU CONTINUAR EXECUTANDO O PROGRAMA

sair = 'N'
soma = contador = media = maior_numero = menor_numero = numero = 0
while sair != 'S':
    numero = int(input('Informe um número: '))
    soma += numero
    contador += 1
    sair = str(input('Deseja sair do programa? [S/N] ')).upper().strip()[0]
    if contador == 1:
        maior_numero = menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

media = soma / contador

print('-=-' * 30)
print('Você digitou {} números.'.format(contador))
print('A soma deles é {}, e a média é {:.2f}.'.format(soma, media))
print('O maior número digitado é {}.'.format(maior_numero))
print('O menor número digitado é {}.'.format(menor_numero))


