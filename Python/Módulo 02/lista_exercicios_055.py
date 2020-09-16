# DESAFIO 055
# ESTRUTURA FOR

# CRIE UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS
# RETORNE O MAIOR PESO
# E TAMBÉM O MENOR PESO

maior_peso = 0
menor_peso = 0
# FOR PRA FAZER O INPUT PRA 5 PESSOAS
for c in range(0, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c + 1)))
    if c == 0:
        # NO PRIMEIRO LAÇO, COMO EU NÃO TENHO PESO NENHUM
        # O PESO QUE EU RECEBI, COMO É ÚNICO
        # PASSA A SER O MAIOR E O MENOR AO MESMO TEMPO
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            # SE O PESO QUE EU LI AGORA É MAIOR QUE O PRIMEIRO (OU ÚLTIMO)
            # ENTÃO O NOVO PESO, PASSA A SER O MAIOR PESO
            maior_peso = peso
        elif peso < menor_peso:
            # SE O PESO QUE EU LI AGORA É MENOR QUE O PRIMEIRO (OU ÚLTIMO)
            # ENTÃO O NOVO PESO, PASSA A SER O MENOR PESO
            menor_peso = peso
print(' ')
print('O maior peso lido é {:.1f}Kg'.format(maior_peso))
print('O menor peso lido é {:.1f}KG'.format(menor_peso))
