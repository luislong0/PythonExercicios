# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

from classe_retangulo import Retangulo

retangulo1 = Retangulo(2, 4)
retangulo1.retornar_valor_lados()
retangulo2 = Retangulo(4, 8)

area1 = retangulo1.calcular_area()
area2 = retangulo2.calcular_area()

perimetro1 = retangulo1.calcular_perimetro()
perimetro2 = retangulo2.calcular_perimetro()

print (area1, area2)
print (perimetro1, perimetro2)

pisos = area2/area1
if (pisos == int(pisos)):
    pisos = pisos
else:
    pisos = int(pisos + 1)

rodape = perimetro2 / perimetro1
if (rodape == int(rodape)):
    final_roda = rodape
else:
    final_roda = int(rodape + 1)

print(f"O total de pisos que tem que ser utilizado é: {pisos}")
print(f"O total de rodapés que tem que ser utilizado é: {rodape}")



