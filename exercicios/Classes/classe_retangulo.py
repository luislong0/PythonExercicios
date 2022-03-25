# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor_lados(self, a, b):
        self.lado_a = a
        self.lado_b = b

    def retornar_valor_lados(self):
        print(self.lado_a)
        print(self.lado_b)

    def calcular_area(self):
        area = self.lado_a * self.lado_b
        return area

    def calcular_perimetro(self):
        primeiro_a = self.lado_a + self.lado_a
        segundo_b = self.lado_b + self.lado_b
        perimetro = primeiro_a + segundo_b
        return perimetro


