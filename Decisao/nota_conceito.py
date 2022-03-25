

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2
conceito = 0

if (media >= 9 and media <= 10):
    conceito = 'A'
    print(conceito)
elif (media >= 7.5 and media < 9):
    conceito = 'B'
    print(conceito)
elif (media >= 6 and media <= 7.5):
    conceito = 'C'
    print(conceito)
elif (media >= 4 and media < 6):
    conceito = 'D'
    print(conceito)
elif (media >= 0 and media < 4):
    conceito = 'E'
    print(conceito)

if (conceito == 'A' or conceito == 'B' or conceito == 'C'):
    print()
    print("Aprovado")
else:
    print()
    print("Reprovado")