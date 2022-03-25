# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

notas = []
soma = 0
media = []
qtdaluno = 0

for i in range(2):
    for j in range(4):
        notas.append(float(input(f'Digite as notas do aluno {i+1}: ')))
        soma = soma + notas[j]
        media = soma / 4
        if (media >= 7.0 and media <= 10.0):
            qtdaluno = qtdaluno + 1
        else:
            qtdaluno = qtdaluno + 0
    print()
print(soma)
print (qtdaluno)