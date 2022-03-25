# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = (int(input('digite um numero correspondente ao dia da semana (1 ao 7) : ')))

if (num == 1):
    print('1 - Domingo')
elif (num == 2):
    print('2 - Segunda feira')
elif (num == 3):
    print('3 - Terça feira')
elif (num == 4):
    print('4 - Quarta feira')
elif (num == 5):
    print('5 - Quinta Feira')
elif (num == 6):
    print('6 - Sexta Feira')
elif (num == 7):
    print('7 - Sabado')
else:
    print('Valor invalido!')