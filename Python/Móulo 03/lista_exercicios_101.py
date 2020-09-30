# DESAFIO 101
# ESTRUTURA FUNÇÕES PARTE 02

# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO()
# QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA
# RETORNANDO UM VALOR LITERAL INDICANDO
# SE UMA PESSO TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES

# FUNÇÃO
def voto(idade):
    # IMPORTAÇÕES
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: Voto Negado!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional!'
    else:
        return f'Com {idade} anos: Voto Obrigatório!'

# PROGRAMA PRINCIPAL
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
print(voto(ano_nascimento))
