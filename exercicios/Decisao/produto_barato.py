# Faça um programa que pergunte o preço de
# três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

numero1 = float(input('Primeiro Preço: '))
numero2 = float(input('Segundo Preço: '))
numero3 = float(input('Terceiro Preço: '))

menor = 0

if (numero1 < numero2 and numero1 < numero3):
    menor = numero1
elif (numero2 < numero1 and numero2 < numero3):
    menor = numero2
elif (numero3 < numero1 and numero3 < numero2):
    menor = numero3

print(f'O produto de menor preço para voce comprar é: R${menor} ')

