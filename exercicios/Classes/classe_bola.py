# Classe Bola: Crie uma classe que modele uma bola:
#
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor
        print(cor)

    def mostra_cor(self):
        print(bola.cor)

coloracao = str(input("Digite a cor da bola: "))
bola = Bola(coloracao, 5, "Borracha")
bola.mostra_cor()
bola.trocaCor("Amarelo")
bola.mostra_cor()

