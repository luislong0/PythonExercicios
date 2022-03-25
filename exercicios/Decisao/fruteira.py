# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

qdt1 = int(input('digite a quantidade de morangos (em Kg): '))
qdt2 = int(input('digite a quantidade de maçãs compradas (em Kg): '))
preco1 = 0
preco2 = 0

pf1= 0
pf2 = 0
pft = 0
pft2 = 0
desc = 0

if (qdt1 < 5 and qdt2 < 5):
    preco1 = 2.50
    preco2 = 1.80
    pf1 = preco1 * qdt1
    pf2 = preco2 * qdt2
    pft = pf1 + pf2
    if (pft > 25):
        desc = (pf1 + pf2) * 0.10
        pft = (pf1 + pf2) - desc
    print (' valor total: {:.2f}'.format(pft))

elif (qdt1 >= 5 and qdt2 >= 5 and qdt1 < 8 and qdt2 < 8):
    preco1 = 2.20
    preco2 = 1.50
    pf1 = preco1 * qdt1
    pf2 = preco2 * qdt2
    pft = pf1 + pf2
    if (pft > 25):
        desc = (pf1 + pf2) * 0.10
        pft = (pf1 + pf2) - desc
    print(' valor total: {:.2f}'.format(pft))

elif (qdt1 >= 8 and qdt2 >= 8):
    preco1 = 2.20
    preco2 = 1.50
    pf1 = preco1 * qdt1
    pf2 = preco2 * qdt2
    desc = (pf1+pf2)*0.10
    pft = (pf1 + pf2) - desc
    print(' valor total: {:.2f}'.format(pft))

