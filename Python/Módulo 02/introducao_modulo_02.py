# FASE 12
# CONDIÇÕES ANINHADAS

# --- TEORIA ---

'''
INTRODUÇÃO E EXPLICAÇÃO

--> IF
--> ELIF
--> ELSE

--- PRÁTICA ---'''

nome = str(input('Qual é o seu nome?   '))
if nome == 'Tales':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'José' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia!, {}'.format(nome))
