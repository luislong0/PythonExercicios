# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []
i = 0
contim = 0
contpar = 0

for i in range(1,11):
    numeros.append(int(input('Digite um numero: ')))

print (numeros)

for i in range(1,10):
    if (numeros[i] % 2) != 0:
        contim = contim + 1
    else:
        contpar = contpar + 1



print (contim)
print (contpar)