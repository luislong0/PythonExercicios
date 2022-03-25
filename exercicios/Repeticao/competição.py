# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e
# depois informe a sua média, conforme a descrição acima informada
# (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
atleta = (input('Digite o nome do atleta: '))
n = int(input('digite a quatidade de jurados: '))
notas = []
j = 0
soma = 0
media = 0
maior = 0
menor = 0
soma2 = 0

# loop das notas e soma
while (j < n):
    notas.append(float(input('digite sua nota: ')))
    soma = soma + notas[j]
    j = j+1

# exibição da soma
print()
for i in range(0,n):
    print(f'notas: {notas[i]}')

maior = max(notas)
menor = min(notas)
soma2 = (soma - maior - menor)
media = soma2/(n-2)

print()
print ('Resultado final:')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {maior}')
print(f'Pior nota: {menor}')
print(f'Media: {media:,.2f}')






