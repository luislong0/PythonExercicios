# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o salario de um colaborador: '))
sal2 = 0

if (salario > 0 and salario < 280):
    sal2 = salario + (salario * 0.20)
    print(f'Salario antes do ajuste: R${salario}')
    print('Percentual de aumento aplicado: 20%')
    print('Valor do aumento = R$', (salario * 0.20))
    print(f'Novo salario = R${sal2}')
elif (salario > 280 and salario < 700):
    sal2 = salario + (salario * 0.15)
    print(f'Salario antes do ajuste: R${salario}')
    print('Percentual de aumento aplicado: 15%')
    print('Valor do aumento = R$', (salario * 0.15))
    print(f'Novo salario = R${sal2}')
elif (salario > 700 and salario < 1500):
    sal2 = salario + (salario * 0.10)
    print(f'Salario antes do ajuste: R${salario}')
    print('Percentual de aumento aplicado: 10%')
    print('Valor do aumento = R$', (salario * 0.10))
    print(f'Novo salario = R${sal2}')
elif (salario > 1500):
    sal2 = salario + (salario * 0.05)
    print(f'Salario antes do ajuste: R${salario}')
    print('Percentual de aumento aplicado: 5%')
    print('Valor do aumento = R$', (salario * 0.05))
    print(f'Novo salario = R${sal2}')

