# Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes:
# alterarNome, depósito e saque; No construtor, saldo é opcional,
# com valor default zero e os demais atributos são obrigatórios

class ContaCorrente:

    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self):
        alt = input("Digite o nome para ser alterado: ")
        self.nome = alt
        return self.nome

    def depositar(self):
        valor = float(input("Digite o valor que voce quer depositar: "))
        self.saldo = self.saldo + valor
        return self.saldo

    def sacar(self):
        valor = float(input("Digite o valor que voce quer depositar: "))
        self.saldo = self.saldo - valor
        return self.saldo