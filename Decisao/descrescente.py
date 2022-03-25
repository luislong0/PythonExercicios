# Faça um Programa que leia três números
# e mostre-os em ordem decrescente.

num1 = int(input('Digite seu primeiro numero: '))
num2 = int(input('Digite seu segundo numero: '))
num3 = int(input('Digite seu terceiro numero: '))

primeiro = 0
segundo = 0
terceiro = 0

if (num1 > num2 and num1 > num3):
    primeiro = num1
elif(num2 > num1 and num2 > num3):
    primeiro = num2
else:
    primeiro = num3

if (num1 > num2 and num1 < num3):
    segundo = num1
elif(num2 > num1 and num2 < num3):
    segundo = num2
else:
    segundo = num3

if (num1 < num2 and num1 < num3):
    terceiro = num1
elif(num2 < num1 and num2 < num3):
    terceiro = num2
else:
    terceiro = num3

print(primeiro)
print(segundo)
print(terceiro)