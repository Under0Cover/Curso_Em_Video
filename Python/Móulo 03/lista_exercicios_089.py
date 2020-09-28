# DESAFIO 089
# ESTRUTURA LISTAS 02

# FAÇA UM PROGRAMA QUE LEIA O NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA
# NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM
# E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE

cadastro_aluno = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota_01 = float(input('Digite a nota do aluno: '))
    nota_02 = float(input('Digite a outra nota do aluno: '))
    media = (nota_01 + nota_02) / 2
    cadastro_aluno.append([nome, [nota_01, nota_02], media])
    resposta = str(input('Deseja cadastrar outro aluno? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        print('Dados inválidos.', end='')
        resposta = str(input('Digite S para cadastrar outro aluno e N para sair: ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=' * 20)
print(f'{"No.":<7}{"NOME":<23}{"MÉDIA":>8}')
print('-=' * 20)
for indice, aluno in enumerate(cadastro_aluno):
    print(f'{indice:<7}{aluno[0]:<23}{aluno[2]:>8.2f}')
while True:
    print('-=' * 20)
    opcao = int(input('Mostrar notas de qual aluno? (999 Sair!): '))
    if opcao == 999:
        print('Processo finalizado!')
        break
    if opcao <= len(cadastro_aluno) - 1:
        print(f'As notas de {cadastro_aluno[opcao][0]} são {cadastro_aluno[opcao][1]}')
print('Volte sempre!')