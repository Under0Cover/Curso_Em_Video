# DESAFIO 040
# ESTRUTURAS IF-ELIF-ELSE

# CRIAR UM PROGRAMA QUE CALCULA A MÉDIA DE UM ALUNO COM 3 RETORNOS
# REPROVAD0
# RECUPERAÇÃO
# APROVADO
# CLÁSSICO ESSE NO IF-ELSE

from time import sleep
nota1 = float(input('Digite a nota do 1º Bimestre: '))
nota2 = float(input('Digite a nota do 2º Bimestre: '))
nota3 = float(input('Digite a nota do 3º Bimestre: '))
nota4 = float(input('Digite a nota do 4º Bimestre: '))
media = float((nota1 + nota2 + nota3 + nota4) /4)
print('A sua média foi de {}'.format(media))
sleep(5)
if media >= 8:
    print('Parabéns, você está APROVADO!')
elif media > 6 and media < 8:
    print('Você está de RECUPERAÇÃO')
else:
    print('Você está REPROVADO!!!')