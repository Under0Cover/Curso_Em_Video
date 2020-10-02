# DESAFIO 112
# ESTRUTURA MÓDULOS

# DENTRO DO PACOTE UTILIDADES_ CURSO_EM_VIDEO QUE CRIAMOS NO DESAFIO 111
# TEMOS UM MÓDULO CHAMADO DADO.
# CRIE UMA FUNÇÃO CHAMADA LEIADINHEIRO()
# QUE SEJA CAPAZ DE FUNCIONAR COMO A FUNÇÃO INPUT()
# MAS COM UMA VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES QUE SEJAM MONETÁRIOS

# IMPORTAÇÕES
from utlidades_curso_em_video.dado import dado
from utlidades_curso_em_video.moeda import moeda

# PROGRAMA PRINCIPAL
numero = dado.leiaDinheiro('Digite um valor em R$: ')
moeda.resumo(numero, 80, 35)