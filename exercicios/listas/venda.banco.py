#Sistema de cadastro e venda de produtos

#importação da hora para o cadastro
from datetime import datetime

#listas/vetores
lista = []
clientes = []
produtos = []
vendas = []

#menu inicial
def menu():
    print ('-' * 30)
    print(print(f'{"Escolha a opção":^30}'))
    print ('-' * 30)
    print('''    [1] Cadastrar Cliente
    [2] Cadastrar produto
    [3] Exibir cliente
    [4] Exibir produto
    [5] Fazer venda
    [6] Exibir venda
    [7] Excluir produto
    [8] Excluir cliente
    [9] Sair do Programa''')
    print()
    opcao = int(input('Digite uma opção: '))
    return opcao


while (True):
    opcao = menu()

    #cadastro cliente
    if (opcao == 1):
        cliente = str(input('Digite o nome do cliente: '))
        clientes.append(cliente)

    #cadastro produto
    elif (opcao == 2):
        produto = str(input('Digite o nome do produto: '))
        produtos.append(produto)

    #exibir clientes
    elif (opcao == 3):
        print(clientes)

    #exibir produtos
    elif (opcao == 4):
        print(produtos)

    #cadastrar venda
    elif (opcao == 5):
        cli = str(input('Digite o nome do cliente: '))
        #validação do cliente
        if (cli in clientes):
            prod = str(input('Digite o nome do produto: '))
            #validação do produto
            if (prod in produtos):
                #cadastrando a hora
                hora = datetime.today().strftime('%Y-%m-%d %H:%M')

                qtd = int(input('Digite a quantidade vendida: '))
                preco = float(input('Digite o valor de cada produto: '))
                vendas.append(f'{hora}, {cli}, {prod}, {qtd}, R${preco*qtd}',)
            else:
                print('-' * 30)
                print('produto invalido')
                print('-' * 30)
        else:
            print('-' * 30)
            print('Cliente invalido')
            print('-' * 30)

    #exibir vendas
    elif (opcao == 6):
        print(vendas)

    #excluir produto
    elif (opcao == 7):
        prodex = str(input('Digite o nome do produto a ser excluido: '))
        # validação do produto
        if (prodex in produtos):
            # remoção de produtos
            produtos.remove(prodex)
        else:
            print('-' * 30)
            print('produto invalido')
            print('-' * 30)

    #excluir cliente
    elif (opcao == 8):
        cliex = str(input('Digite o nome do cliente a ser excluido: '))
        # validação do cliente
        if (cliex in clientes):
            #remoção de clientes
            clientes.remove(cliex)
        else:
            print('-' * 30)
            print('Cliente invalido')
            print('-' * 30)

    #finalizar produto
    elif (opcao == 9):
        break