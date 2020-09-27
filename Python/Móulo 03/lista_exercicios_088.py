# DESAFIO 088
# ESTRUTURA LISTAS 02

# DESAFIO DA MEGA SENA
# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES
# O PROGRAMA DEVE PERGUNTAR QUANTOS JOGOS SERÃO GERADOS
# APOS DEVE SORTEAR 6 NUMEROS ENTRE 1 E 60
# CADASTRANDO TUDO EM UMA LISTA COMPOSTA

from random import randint
from time import sleep
print('-=-' * 20)
print(' ' * 20, 'JOGOS DA MEGA SENA')
print('-=-' * 20)
aposta = []
jogos = []
total_jogos = 1
quantidade = int(input('Quantos jogos você quer fazer? '))
while total_jogos <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in aposta:
            aposta.append(numero)
            contador += 1
        if contador >= 6:
            break
    aposta.sort()
    jogos.append(aposta[:])
    aposta.clear()
    total_jogos += 1
print(f'Sortear {quantidade} jogos!')
sleep(3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
print('Todos os jogos sorteados!')
sleep(1)
print('Boa sorte!!!')
