# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer_pessoa(self, idade):
        idade = idade + 1
        self.idade = idade
        if (self.idade < 21):
            self.altura = self.altura + 0.05
        return self.idade

    def engordar_pessoa(self, peso):
        eng = float(input("Digite quantos kilos a pessoa vai engordar: "))
        eng = peso + eng
        self.peso = eng
        return self.peso

    def emagrecer_pessoa(self, peso):
        ema = float(input("Digite quantos kilos a pessoa vai emagrecer: "))
        ema = peso - ema
        self.peso = ema
        return self.peso

    def crescer_pessoa(self, altura):
        cres = float(input("Digite quanto que a pessoa cresceu: "))
        cres = altura + cres
        self.altura = cres
        return self.altura

_nome = input("Digite o nome da pessoa: ")
_idade = int(input("Digite a idade da pessoa: "))
_peso = float(input("Digite o peso da pessoa: "))
_altura = float(input("Digite a altura da pessoa: "))
pessoa = Pessoa(_nome, _idade, _peso, _altura)


pessoa.envelhecer_pessoa(pessoa.idade)
pessoa.engordar_pessoa(pessoa.peso)
pessoa.emagrecer_pessoa(pessoa.peso)
pessoa.crescer_pessoa(pessoa.altura)

print()
print(pessoa.idade)
print(pessoa.peso)
print(pessoa.altura)
