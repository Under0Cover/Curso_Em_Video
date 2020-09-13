# DESAFIO 044
# ESTRUTURAS IF-ELIF-ELSE

# ELABORAR UM PROGRAMA QUE DÊ DESCONTOS E/OU ACRÉSCIMOS DEPENDENDO DA FORMA DE PAGAMENTO

print('Loja da Márcia')
print('Escolha a forma de pagamento:')
print('1- Dinheiro/Cheque:')
print('2- Cartão:')
print('3- 2x Cartão:')
print('4- 3+x Cartão:')
forma_pagamento = int(input('-> '))
if forma_pagamento == 1:
    print('Você terá 10% de desconto!')
elif forma_pagamento == 2:
    print('Você terá 5% de desconto!')
elif forma_pagamento == 3:
    print(' ')
elif forma_pagamento == 4:
    print('Será adicionado 20% pelo parcelamento!')
else:
    print('Opção inválida!!!')
preco = float(input('Informe o preço R$: '))
if forma_pagamento == 1:
    valor = (preco - (preco * 0.1))
elif forma_pagamento == 2:
    valor = (preco - (preco * 0.05))
elif forma_pagamento == 3:
    valor = preco
else:
    valor = (preco + (preco * 0.2))
print('O seu total geral é de R$ {:.2f}'.format(valor))