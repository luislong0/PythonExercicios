# Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.


base = int(input('Digite o valor da base: '))
expo = int(input('Digite o valor do expoente: '))


r = 1
i = 0

while (i < expo):
    r = r * base
    i += 1

if (expo == 0):
        print (1)
else:
    print(r)



