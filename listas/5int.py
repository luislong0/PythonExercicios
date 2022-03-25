# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

qtd = (int(input('Digite a quantidade: ')))
numeros = []
i = 0

while (i < qtd):
    numeros.append(int(input('Digite um numero: ')))
    i = i + 1

for j in range(0 , qtd):
    print (numeros[j])
