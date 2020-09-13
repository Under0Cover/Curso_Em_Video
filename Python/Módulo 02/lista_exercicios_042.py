# DESAFIO 042
# ESTRUTURAS IF-ELIF-ELSE

# USANDO COMO BASE O EXERCÍCIO 039
# REMONTE-O
# ALÉM DE DAR AS MEDIDAS DIZENDO SE ELAS PODEM OU NÃO CONSTRUIR UM TRIÂNGULO
# AGORA QUANDO ELAS PUDEREM
# DIGA QUAL TRIÂNGULO PODE SER FORMADO
# 3 RETORNOS
# EQUILÁTERO : TODOS OS LADOS IGUAIS
# ISÓSCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
if lado1 < (lado2 + lado3) and lado2 < (lado3 + lado1) and lado3 < (lado1 + lado2):
    print('Essas medidas podem construir um triângulo!')
    if (lado1 == lado2 == lado3):
        print('Esse triângulo é um Triângulo Equilátero')
    elif (lado1 == lado2 != lado3):
        print('Esse triângulo é um Triângulo Isósceles')
    else:
        print('Esse triângulo é um Triângulo Escaleno')
else:
    print('Essas medidas não podem construir um triângulo!')