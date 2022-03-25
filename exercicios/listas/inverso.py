# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

qtd = (int(input('Digite a quatidade de numeros: ')))
numeros = []


for i in range(1,qtd + 1):
    numeros.append(int(input('Digite um numero: ')))

numeros.reverse()
numeros

print (numeros)