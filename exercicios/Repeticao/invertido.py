# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido

numero = int(input('Digite um numero: '))
numero = str(numero)

vetor = []

for i in numero:
    vetor.append(i)

print(vetor[::-1])