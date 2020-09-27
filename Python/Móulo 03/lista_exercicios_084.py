# DESAFIO 084
# ESTRUTURA LISTAS 02

#
# FAÇA UM PROGRAMA QUE LEIA O NOME E PESO DE VÁRIAS PESSOAS
# GUARDANDO TUDO EM UMA LISTA
# NO FIM ME DÊ 03 RETORNOS:
# A) QUANTAS PESSOAS FORAM CADASTRADAS
# B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES

dados_final = []
# ESSA SERÁ A LISTA FINAL
aprovacao = []
# ESSA SERÁ A LISTA QUE IREI UTILIZAR PARA ANALISAR OS DADOS
menor_peso = maior_peso = 0
# VARIAVEIS PARA MAIOR E MENOR PESOS
while True:
    aprovacao.append(str(input('Digite o nome: ')))
    # INPUT RECEBENDO O NOME
    aprovacao.append(float(input('Digite o peso: ')))
    # INPUT RECEBENDO O PESO
    if len(dados_final) == 0:
        # SE FOR A PRIMEIRA LEITURA DE DADOS
        maior_peso = menor_peso = aprovacao[1]
        # CONSIDERAR O MAIOR E O MENOR COMO IGUAIS AO PRIMEIRO DADO
    else:
        # CASO NÃO SEJA O PRIMEIRO DADO
        if aprovacao[1] > maior_peso:
            # VOU VERIFICAR SE ELE É MAIOR DO QUE O ÚLTIMO RECEBIDO
            maior_peso = aprovacao[1]
            # CASO SEJA, JÁ VOU GUARDAR ELE COMO MAIOR
        elif aprovacao[1] < menor_peso:
            # CASO ELE SEJA O MENOR DO QUE O ÚLTIMO RECEBIDO
            menor_peso = aprovacao[1]
            # CASO SEJA O MENOR, EU VOU ARMAZENAR ELE NA VARIAVEL MENOR PESO
    dados_final.append(aprovacao[:])
    # AQUI EM ARMAZENO DE FORMA LIVRE OS DADOS NA LISTA FINAL
    aprovacao.clear()
    # EU ZERO LISTA APROVACAO PARA REAPROVEITO
    sair = str(input('Deseja sair? [S/N]: ')).upper().strip()[0]
    # AQUI EU PROCURO A CONTINUIDADE DE DADOS PELO USUÁRIO
    while sair not in 'SN':
        # O USUARIO NÃO PODERÁ SAIR DO LAÇO ENQUANTO NÃO DIGITAR A RESPOSTA ESPERADA
        sair = str(input('Dados incorretos! Digite S para sair e N para adicionar outros dados: ')).upper().strip()[0]
        # REFORÇO DA CONTINUIDADE
    if sair == 'S':
        # CASO ELE DESEJA SAIR DO PROGRAMA
        break
        # BREAK PARA INTERROMPER LAÇO INFINITO
print(f'A lista contém {len(dados_final)} dados cadastrados!')
# RESPOSTA DA LETRA A, EXIBINDO O VALOR NUMERICO TOTAL
print(f'O menor peso foi {menor_peso} KG de ', end='')
# AQUI A SAIDA COM MENOR PESO
for pessoas in dados_final:
    # UM FOR PARA PROCURAR PESSOAS COM O MESMO PESO MENOR DIGITADO
    if pessoas[1] == menor_peso:
        # A CONDICAO DE IGUALDADE PARA COMPARACAO
        print(f'[{pessoas[0]}] ', end='')
        # A SAIDA FINAL
print('.')
# FORMATACAO
print(f'O maior peso foi {maior_peso} KG de ', end='')
# AQUI A SAIDA COM MAIOR PESO
for pessoas in dados_final:
    # UM FOR PARA PROCURAR PESSOAS COM O MESMO PESO MAIOR
    if pessoas[1] == maior_peso:
        # A CONDICAO DE IGUALDADE PARA COMPARACAO
        print(f'[{pessoas[0]}] ', end='')
        # A SAIDA FINAL
print('.')
# FORMATACAO

# RESPOSTA DO EXERCICIO COM COMENTARIO PARA RESPOSTA NO FORUM DA FACULDADE SOBRE PYTHON
# O FORUM EXIGIA UMA LISTA E UM FOR