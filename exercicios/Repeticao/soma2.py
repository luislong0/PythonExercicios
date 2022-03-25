# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# Altere o programa anterior para mostrar no final a soma dos números.

numero1= int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
soma = 0

while (numero2 < numero1):
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite outro numero: '))

for i in range(numero1 + 1, numero2, 1):
    soma = (soma + i)

print(soma)