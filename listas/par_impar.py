# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

numeros = []
par = []
imp = []

for i in range(20):
    numeros.append(int(input('Digite um numero: ')))

for j in range(20):
    if (numeros[j] % 2 == 0):
        par.append(numeros[j])
    else:
        imp.append(numeros[j])

print (f'Numeros: {numeros}')
print (f'Numeros pares: {par}')
print (f'Numeros impares: {imp}')