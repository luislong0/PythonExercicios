# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um numero: '))

if num > 1:

    for i in range(2, num):

        if (num % i) == 0:
            print(num, " é nao primo")
            break
    else:
        print(num, "é primo")

else:
    print(num, "é nao primo")