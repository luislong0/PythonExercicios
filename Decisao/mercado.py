tipo = (input('Insira o tipo da carne comprada: '))
qtdcarne = float(input('Insira a quantidade de carne comprada em (Kg): '))

fileduplo = 0
alcatra = 0
picanha = 0

total = 0


cartao = (input('Irá utilizar o cartão tabajara para a compra ou outro meio de pagamento? : '))
desconto = 0.05
comdesc = 0

if (tipo == 'file duplo' and qtdcarne < 5):
    fileduplo = 4.90
    total = (fileduplo*qtdcarne)
    if (cartao == 'sim'):
        comdesc = total - (total*desconto)
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto: {:.2f} '.format(total*desconto))
        print(f'Valor a pagar: {comdesc}')
    else:
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto: R$ 0.00',)
        print (total)

elif (tipo == 'alcatra' and qtdcarne < 5):
    alcatra = 5.90
    total = (alcatra*qtdcarne)
    if (cartao == 'sim'):
        comdesc = total - (total * desconto)
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto: {:.2f} '.format(total * desconto))
        print(f'Valor a pagar: {comdesc}')
    else:
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto: R$ 0.00', )
        print(total)

elif (tipo == 'picanha' and qtdcarne < 5):
    picanha = 6.90
    total = (picanha*qtdcarne)
    if (cartao == 'sim'):
        comdesc = total - (total * desconto)
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto: {:.2f} '.format(total * desconto))
        print(f'Valor a pagar: {comdesc}')
    else:
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto: R$ 0.00', )
        print(total)

elif (tipo == 'file duplo' and qtdcarne > 5):
    fileduplo = 5.80
    total = (fileduplo*qtdcarne)
    if (cartao == 'sim'):
        comdesc = total - (total * desconto)
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto com o desconto da quantidade da carne atribuido: {:.2f} '.format(total * desconto))
        print(f'Valor a pagar: {comdesc}')
    else:
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto da quantidade da carne')
        print(total)

elif (tipo == 'alcatra' and qtdcarne > 5):
    alcatra = 5.90
    total = (alcatra*qtdcarne)
    if (cartao == 'sim'):
        comdesc = total - (total * desconto)
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto com o desconto da quantidade da carne atribuido: {:.2f} '.format(total * desconto))
        print(f'Valor a pagar: {comdesc}')
    else:
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto da quantidade da carne')
        print(total)

elif (tipo == 'picanha' and qtdcarne > 5):
    picanha = 5.90
    total = (picanha*qtdcarne)
    if (cartao == 'sim'):
        comdesc = total - (total * desconto)
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto com o desconto da quantidade da carne atribuido: {:.2f} '.format(total * desconto))
        print(f'Valor a pagar: {comdesc}')
    else:
        print(f'Tipo da carne: {tipo}')
        print(f'Quantidade: {qtdcarne}')
        print(f'Preço total: {total}')
        print(f'Tipo de pagamento: {cartao}')
        print('Desconto atribuido na quantidade da carne')
        print(total)
#
