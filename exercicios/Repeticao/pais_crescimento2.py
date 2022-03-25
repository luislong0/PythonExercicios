paisA = int(input('Digite a população do primeiro pais: '))
paisB = int(input('Digite a população do segundo pais: '))
taxaA = float(input('Digite a taxa de crescimento do primeiro pais: '))
taxaB = float(input('Digite a taxa de crescimento do segundo pais: '))
ano = 0

while paisA < paisB:
    if(paisA < paisB):
        paisA = (paisA + (paisA * taxaA))
        paisB = (paisB + (paisB * taxaB))
        ano = ano +1

print (ano)