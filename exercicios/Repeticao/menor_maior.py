# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input('digite a quatidade de numeros: '))
numeros = []
j = 0
maior = 0
menor = 0

while (j < n):
    numeros.append(int(input('digite um numero: ')))
    if j == 0:
        maior = menor = numeros[j]
    else:
        if numeros[j] > maior:
                maior = numeros[j]
        if numeros[j] < menor:
                menor = numeros[j]
    j = j+1

print (maior)
print (menor)





