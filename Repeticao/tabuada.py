# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

numero = int(input('Digite um numero de 1 a 10: '))
tabuada = 0

while (numero < 1 or numero > 10):
    numero = int(input('Digite um numero de 1 a 10: '))

for i in (range(0,11)):
    tabuada = (numero * i )
    print (f' {numero} X {i} = {tabuada}')

