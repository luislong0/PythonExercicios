# Faça um programa que leia 5 números e informe o maior número

numeros = []
for i in range(1,6):
    numeros.append(int(input('Digite um numero: ')))

maiornum = numeros[0]
cont = 1

while cont < len(numeros):
    if numeros[cont] > maiornum:
        maiornum = numeros[cont]
    cont = cont + 1

print ('O maior numero é: ', maiornum)