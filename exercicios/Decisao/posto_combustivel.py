# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
#
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
#
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = int(input('Numero de litros: '))
tipo = input('Tipo de combustivel (A-álcool, G-gasolina): ')

precoal = 0
precogas = 0
desconto = 0
final = 0

print(litros * 1.90)

if (tipo == 'A' and litros < 20):
    desconto = 1.90 - (1.90 * 0.03)
    precoal = litros * desconto
    print(f'Valor a pagar: R${precoal}')
elif (tipo == 'A' and litros > 20):
    desconto = 1.90 - (1.90 * 0.05)
    print(f'f desconto: {desconto}')
    precoal = litros * desconto
    print(f'Valor a pagar: R${precoal}')
elif (tipo == 'G' and litros < 20):
    desconto = 2.50 - (2.50 * 0.04)
    precogas = litros * desconto
    print(f'Valor a pagar: R${precogas}')
elif (tipo == 'G' and litros > 20):
    desconto = 2.50 - (2.50 * 0.06)
    precogas = litros * desconto
    print(f'Valor a pagar: R${precogas}')







