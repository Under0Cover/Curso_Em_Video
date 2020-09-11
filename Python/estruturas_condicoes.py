# --- TEORIA ---
# CONDIÇÕES

# EXPLICAÇÃO DO IF ELSE

# PRATICANDO IF-ELSE

nome = str(input('Qual é o seu nome? '))
if nome == 'Tales':
    print('Que nome lindo você tem!')
else:
    print('Humm.... Nome comum...')
print('Bom dia, {}!'.format(nome))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média foi {:.2f}'.format(media))
if media >= 7.0:
    print('Sua média foi boa, CONTINUE ASSIM')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')