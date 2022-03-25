# Faça um Programa que leia três números e mostre o
# maior e o menor deles.

numero1 = int(input('Primeiro Numero: '))
numero2 = int(input('Segundo Numero: '))
numero3 = int(input('Terceiro Numero: '))
maior = 0
menor = 0

if (numero1 > numero2 and numero1 > numero3):
    maior = numero1
elif (numero2 > numero1 and numero2 > numero3):
    maior = numero2
elif (numero3 > numero1 and numero3 > numero2):
    maior = numero3

print(f'Maior numero: {maior}')

if (numero1 < numero2 and numero1 < numero3):
    menor = numero1
elif (numero2 < numero1 and numero2 < numero3):
    menor = numero2
elif (numero3 < numero1 and numero3 < numero2):
    menor = numero3

print(f'Menor numero: {menor}')

