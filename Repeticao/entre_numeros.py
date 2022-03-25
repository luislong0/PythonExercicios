# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.


numero1= int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

while (numero2 < numero1):
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite outro numero: '))

for i in range(numero1 + 1, numero2, 1):
    print (i)
