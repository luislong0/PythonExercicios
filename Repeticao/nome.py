# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# nome

nome = input('Insira um nome: ')

while (len(nome) <= 3):
    nome = input('Insira um nome: ')

print()
print(nome)
print()

#idade

idade = int(input('Insira uma idade: '))

while (idade < 0 or idade > 150):
    idade = int(input('Insira uma idade: '))

print()
print(idade)
print()

#salario

sal = float(input('Digite seu salario: '))

while (sal < 0):
    float(input('Digite seu salario: '))

print()
print(f'salario: R${sal}')
print()

#sexo

sexo = str(input('Digite seu Sexo (f ou m): '))


while (sexo != "f" and sexo != "m"):
        sexo = str(input('Digite seu Sexo (f ou m): '))

if(sexo == 'f'):
    sexo2 = 'Feminino'
elif (sexo == 'm'):
    sexo2 = 'Masculino'

print()
print(f'Sexo: {sexo2}')
print()

# Estado Civil: 's', 'c', 'v', 'd';

std = str(input('Estado Civil: s, c, v, d: '))
std2 = 0

while (std != "s" and std != "c" and std != "v" and std != "d"):
        std = str(input('Estado Civil: s, c, v, d: '))

if(std == 's'):
    std2 = 'Solteiro'
elif (std == 'c'):
    std2 = 'Casado'
elif (std == 'v'):
    std2 = 'Viuvo(a)'
elif (std == 'd'):
    std2 = 'Divorciado Comedor de casada'

print()
print(f'Estado Civil: {std2}')
print()