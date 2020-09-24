# DESAFIO 077
# TUPLAS

# CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS SEM ACENTOS
# DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA
# QUAIS SÃO AS SUAS VOGAIS

lista_palavras = ('aprender', 'programar', 'linguagem', 'python',
                  'curso', 'gratis', 'estudar', 'praticar',
                  'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in lista_palavras:
    # SEPARANDO AS PALAVRAS
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    # PRINT DAS PALAVRAS
    for letra in palavra:
        # SEPARANDO AS LETRAS
        if letra.lower() in 'aeiou':
            # COMPARAR AS LETRAS SEPARADAS COM AS QUE EU QUERO
            print(letra, end=' ')
            # PRINT NAS SELECIONADAS
