# DESAFIO 103
# ESTRUTURA FUNÇÕES 02

# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA()
# QUE RECEBA DOIS PARÂMETROS OPCIONAIS:
# O NOME DE UM JOGADOR
# A QUANTIDADE DE GOLS QUE ELE MARCOU
# O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR
# MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE

# FUNÇÕES
def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no Campeonato!')


# PROGRAMA PRINCIPAL
nome_jogador = str(input('Nome do jogador: '))
# COMO O PROGRAMA PERMITE A NÃO INSERÇÃO DE DADOS
gols_jogador = str(input('Número de gols feitos: '))
# COMO O PROGRAMA PERMITE A NÃO INSERÇÃO DE DADOS
# TRATAMOS O GOLS_JOGADOR COMO STRING PARA PODER RECEBER VAZIO
if nome_jogador.strip() == '':
    ficha(gol=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)
# A MINHA INTENÇÃO ERA COLOCAR O GOLS_JOGADOR AQUI
# MAS O PROGRAMA ACUSA ERRO
if gols_jogador.isnumeric():
    # SE O VALOR DIGITADO É NUMÉRICO
    gols_jogador = int(gols_jogador)
    # A VARIÁVEL VAI RECEBER SEU INTEIRO
else:
    # CASO O VALOR NÃO SEJA NUMÉRICO
    gols_jogador = 0
    # VOU ATRIBUIR O VALOR ZERO COMO PARÂMETRO
