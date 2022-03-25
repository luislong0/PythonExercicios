# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []
for i in range(1,6):
    numeros.append(int(input('Digite um numero: ')))


soma = 0
cont = 0
media = 0

while cont < len(numeros):
        soma = numeros[cont] + soma
        cont = cont + 1

media = soma / cont


print (soma)
print (media)