# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
# Altere o programa de cálculo do fatorial, permitindo ao usuário
# calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

numero = int(input('Digite um numero para ser verificado: '))
numero2 =0
fator = 1
cont = 1

while numero > 0 and numero <= 16:
        numero2 = int(input('Digite um numero para ser fatorado: '))
        while (cont <= numero2):
            if (numero2 > 0 and numero2 <= 16):
                fator = fator * cont
                cont = cont + 1
            else:
                quit()
        print (fator)
