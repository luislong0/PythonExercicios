down = int(input('Tamanho de download (MB): '))
velo = int(input('Velocidade de internet (Mbps): ' ))

tempo = down / velo
tempoM = tempo * 60

print(f'f Tempo de download aproximado em minutos: {tempoM} minutos')