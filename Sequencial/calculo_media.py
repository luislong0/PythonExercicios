cont = 0
notafinal = 0
while cont < 4:
    nota = float(input('Digite sua nota:'))
    notafinal = notafinal + nota
    cont += 1

media = notafinal/cont
print(media)
