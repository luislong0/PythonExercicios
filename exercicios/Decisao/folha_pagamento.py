# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
# para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
# Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220


valor = float(input('Digite quanto voce ganha por hora: '))
hora = int(input('Digite quantas horas trabalhadas por mes: '))

salbruto = (valor*hora)
ir = 0
inss = 0
fgts = 0
totald = 0
saliq = 0

print(f'Salario bruto: ({valor} * {hora}): R${salbruto}')

if(salbruto > 0 and salbruto <= 900):
    print('insento')
elif(salbruto > 900 and salbruto <= 1500):
    ir = (salbruto * 0.05)
    print(f'(-) IR (5%) : R${ir}')
elif(salbruto > 1500 and salbruto <= 2500):
    ir = (salbruto * 0.10)
    print(f'(-) IR (10%) : R${ir}')
elif (salbruto > 2500):
    ir = (salbruto * 0.20)
    print(f'(-) IR (20%) : R${ir}')

inss = (salbruto * 0.10)
print(f'(-) INSS (10%) : R${inss}')

fgts = (salbruto * 0.11)
print(f'FGTS (11%) : R${fgts}')

totald = (ir+inss)
print(f'Total de descontos : R${totald}')

saliq = (salbruto - totald)
print(f'Salario Liquido : R${saliq}')





