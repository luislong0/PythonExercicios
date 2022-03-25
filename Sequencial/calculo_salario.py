por_hr = float(input('Quanto você ganha por hora?: '))
horas = int(input('Horas trabalhadas por mês: '))
bruto = por_hr * horas
print(f'+Salario bruto: R${bruto}')

ir = bruto * 0.11

print(f'-IR (11%): R${ir}')

inss = bruto * 0.08

print(f'-INSS (8%): R${inss}')

sind = bruto * 0.05

print(f'-Sindicato (5%) : R${sind}')

liquido = bruto - ir - inss - sind

print(f'=Salário Liquido: R${liquido}')

