# CORES NO PYTHON

'''
STYLE       -> OPÇÕES:
    0       -> NONE
    1       -> BOLD
    4       -> UNDERLINE
    7       -> NEGATIVE

TEXT        -> OPÇÕES:
    30      -> BRANCO
    31      -> VERMELHO
    32      -> VERDE
    33      -> AMARELO
    34      -> AZUL
    35      -> MAGENTA
    36      -> CIANO
    37      -> CINZA

BACK        -> OPÇÕES:
    40      -> BRANCO
    41      -> VERMELHO
    42      -> VERDE
    43      -> AMARELO
    44      -> AZUL
    45      -> MAGENTA
    46      -> CIANO
    47      -> CINZA

MODO DE USO: \033[STYLE;TEXT;BACKm

# Exemplos:
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[0;30;42m
\033[m
\033[7;30m

'''

print('\033[31mOlá, Mundo!')
print('\033[0;30;41mOlá, Mundo Colorido...')
print('\033[4;33;44mBrincando com as cores')
print('\033[1;35;43mDá pra fazer assim também, oh\033[m')
print('\033[0;30;42mÉ meio estranho essas paradas, né?!')
print('\033[7;30mTenho certeza de que não está bonito...\033[m')
print('\033[1;34;40mDane-se, não sou Desginer...')

