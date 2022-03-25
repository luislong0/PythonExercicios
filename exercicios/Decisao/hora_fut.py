hora_1 = int(input('digite a hora que voce entrou: '))
minutos_1 = int(input('digite os minutos que voce entrou: '))
hora_2 = int(input('digite a hora que voce saiu: '))
minutos_2 = int(input('digite os minutos que voce saiu: '))

final = (hora_2-hora_1)
final2 = (minutos_2 - minutos_1)

if (final < 0 and final2 < 0):
    final = (final + 23)
    final2 = (final2 + 60)
    print(f' hora jogadas foi: {final}:{final2} ')

elif (final2 < 0):
        final = (final-1)
        final2 = (final2 + 60)
        print(f' hora jogadas foi: {final}:{final2} ')

elif (final < 0 ):
        final = (final + 24)

        print(f' hora jogadas foi: {final}:{final2} ')

else :
    print(f' hora jogadas foi: {final}:{final2} ')


