# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input('digite a quatidade de numeros: '))
numeros = []
numeroscertos = list(range(1,1000))
j = 0
maior = 0
menor = 0

while (j < n):
    numeros.append(int(input('digite um numero: ')))

    j = j + 1

print (min(numeros))
print (max(numeros))