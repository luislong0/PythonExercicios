# Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        #tamanho do lado
        self.lado = lado

    def mudar_valor_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_valor_lado(self):
        print(self.lado)

    def calcular_area_lado(self):
        lado_area = self.lado
        area = lado_area * lado_area
        print (area)

side = float(input("Digite o valor do lado do quadrado: "))
quadrado = Quadrado(side)
print(quadrado.lado)
quadrado.retornar_valor_lado()
quadrado.calcular_area_lado()
quadrado.mudar_valor_lado(6.5)
quadrado.retornar_valor_lado()
quadrado.calcular_area_lado()