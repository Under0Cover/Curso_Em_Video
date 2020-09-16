# DESAFIO 062
# ESTRUTURA WHILE

# MELHORAR O EXERCÍCIO 061 DE PA
# DANDO A OPÇÃO DE MOSTRAR MAIS TERMOS
# DANDO A ESCOLHA DA QUANTIDADE DE TERMOS PRO USUÁRIOS ESCOLHER

print('Cálculo de Progressão Aritmética')
prim_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da Progressão: '))

termo = prim_termo
contador = 1
total_termos = 0
ver_a_mais = 10

while ver_a_mais != 0:
    total_termos = total_termos + ver_a_mais
    while contador <= total_termos:
        print('{} -'.format(termo), end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    ver_a_mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total_termos))
print('\nFIM DO PROGRAMA')
