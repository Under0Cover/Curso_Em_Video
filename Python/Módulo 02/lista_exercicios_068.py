# DESAFIO 068
# ESTRUTURA WHILE COM BREAK

# FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR
# O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER
# MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS

from random import randint

print('-=-' * 20)
print('Vamos jogar par ou impar')
print('-=-' * 20)
jogos_vencidos = 0

while True:
    numero_pessoa = int(input('Digite um valor: '))
    escolha = str(input('Você quer par ou impar? [P/I]: ')).upper().strip()[0]
    print('-=-' * 20)
    numero_pc = randint(0, 10)
    resultado = numero_pc + numero_pessoa
    if resultado % 2 == 0:
        print(f'Você jogou {numero_pessoa} e o computador jogou {numero_pc}.')
        print(f'O total foi de {resultado}, PAR')
        final = 'P'
        print('-=-' * 20)
    else:
        print(f'Você jogou {numero_pessoa} e o computador jogou {numero_pc}.')
        print(f'O total foi de {resultado}, IMPAR')
        final = 'I'
        print('-=-' * 20)
    if escolha == final:
        print('VOCÊ VENCEU!!!!!')
        jogos_vencidos += 1
    elif escolha != final:
        print('VOCÊ PERDEU!!!!!')
        break
print('GAME OVER')
print(f'Você venceu {jogos_vencidos} jogos.')
print('-=-' * 20)
