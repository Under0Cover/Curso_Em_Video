# DESAFIO 105
# ESTRUTURA FUNÇÃO 02

# FAÇA UM PROGRAMA QUE TENHA A FUNÇÃO NOTAS()
# QUE PODERÁ RECEBER VÁRIAS NOTAS DE ALUNOS
# E VAI RETORNAR UM DICONÁRIO COM AS SEGUINTES INFORMAÇÕES:
# - QUANTIDADE DE NOTAS
# - A MAIOR NOTA
# - A MENOR NOTA
# - A MÉDIA DAS NOTAS
# - A SITUAÇÃO (OPCIONAL)
# ADICIONTE TAMBÉM AS DOCSTRINGS

# FUNÇÕES
def notas(*nota, situacao=False):
    """
    -> Função para análise e situações
    :param nota: Entrada de notas de um ou vários alunos
    :param situacao: Opcional, situação variável conforme média total
    :return: Dicionário completo e detalhado das notas
    """
    historico = dict()
    historico['Total'] = len(nota)
    historico['Maior'] = max(nota)
    historico['Menor'] = min(nota)
    historico['Média'] = sum(nota) / len(nota)
    if situacao:
        if historico['Média'] >= 9:
            historico['Situação'] = 'Exemplar'
        elif historico['Média'] >= 8:
            historico['Situação'] = 'Muito Boa'
        elif historico['Média'] >= 7:
            historico['Situação'] = 'Boa'
        elif historico['Média'] >= 6:
            historico['Situação'] = 'Aceitável'
        elif historico['Média'] >= 5:
            historico['Situação'] = 'Ruim'
        elif historico['Média'] >= 3:
            historico['Situação'] = 'Complicada'
        else:
            historico['Situação'] = 'Preocupante'
    return historico


# PROGRAMA PRINCIPAL
resposta = notas(10, 9.75, situacao=True)
print(resposta)