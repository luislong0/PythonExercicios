# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

char = []
consoante = 0
consoantes = []

for i in range(10):
    char.append(str(input(f'Caracter {i +1}: ')))
    if (char[i] != 'a' and char[i] != 'e' and char[i] != 'i' and char[i] != 'o' and char[i] != 'u'):
        consoantes.append(char[i])
        consoante = consoante + 1

print (f'Consoantes digitadas: {consoantes}')
print (f'Quantifade de consoantes: {consoante}')