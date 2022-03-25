#Sistema de cadastro e venda de produtos

#importação da hora para o cadastro
from datetime import datetime
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-PMKKLEA\SQLEXPRESS;"
    "Database=SoftVendas;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

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
    print('''[1] Cadastrar Cliente
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
        id = int(input('Digite o Id do cliente: '))
        cliente = str(input('Digite o nome do cliente: '))
        comando = f"""INSERT INTO Clientes(id_cli, cliente) VALUES({id}, '{cliente}')"""
        print(comando)
        cursor.execute(comando)
        cursor.commit()

    #cadastro produto
    elif (opcao == 2):
            id2 = int(input('Digite o Id do Produto: '))
            produto = str(input('Digite o nome do produto: '))
            qtd = int(input('Digite a quantidade do produto: '))
            comando = f"""INSERT INTO Produtos(id_produto, quantidade, produto) VALUES({id2}, '{qtd}', '{produto}')"""
            print(comando)
            cursor.execute(comando)
            cursor.commit()

    #exibir clientes
    elif (opcao == 3):
        selecao = f"""select * from Clientes"""
        cursor.execute(selecao)
        linhas = cursor.fetchall()
        cursor.commit()

        for linha in linhas:
            print("id_cli:", linha[0])
            print("cliente:", linha[1])
            print()

    # exibir produtos
    elif (opcao == 4):
      selecao = f"""select * from Produtos"""
      cursor.execute(selecao)
      linhas = cursor.fetchall()
      cursor.commit()

      for linha in linhas:
          print("id_produto:", linha[0])
          print("quantidade de produto:", linha[1])
          print("produto:", linha[2])
          print()

    # Cadastro de Vendas
    elif (opcao == 5):
        print('-' * 40)
        print("Digite um cliente cadastrado no sistema")
        print('-' * 40)
        cli = str(input('Digite o nome do cliente: '))
        selecao = f"""select cliente from Clientes WHERE cliente = '{cli}'"""
        cursor.execute(selecao)
        linhas = cursor.fetchall()
        cursor.commit()

        for linha in linhas:
            varcli = linha[0]
        varcli_str = str(varcli)
        if (cli == varcli_str):
            print('-' * 40)
            print("Digite um produto cadastrado no sistema")
            print('-' * 40)
            prod = str(input('Digite o nome do produto: '))
        #validação do produto

            selecao = f"""SELECT produto FROM Produtos WHERE produto = '{prod}' """
            cursor.execute(selecao)
            linhas = cursor.fetchall()
            cursor.commit()

            for linha in linhas:
                varprod = linha[0]
            varprod_str = str(varprod)
            if (prod in varprod_str):
                #cadastrando a hora
                hora = datetime.today().strftime('%Y-%m-%d %H:%M')
                id_venda = int(input('Digite o ID da venda: '))
                qtd = int(input('Digite a quantidade vendida: '))
                preco = float(input('Digite o valor de cada produto: '))
                comando = f"""INSERT INTO Vendas(id_venda, data_venda, cliente, produto, quantidade, preco, valor_total) VALUES('{id_venda}', '{hora}', '{varcli_str}', '{varprod_str}', '{qtd}', '{preco}', '{preco*qtd}')"""
                print(comando)
                cursor.execute(comando)
                cursor.commit()

    # exibir vendas
    elif (opcao == 6):
        selecao = f"""select * from Vendas"""
        cursor.execute(selecao)
        linhas = cursor.fetchall()
        cursor.commit()

        for linha in linhas:
            print("id_venda:", linha[0])
            print("data_venda:", linha[1])
            print("cliente:", linha[2])
            print("produto:", linha[3])
            print("Quantidade:", linha[4])
            print("Preco: R$", linha[5])
            print("valor_total: R$", linha[6])
            print()

    # excluir produto
    elif (opcao == 7):
        print('-' * 40)
        print("Digite um produto cadastrado no sistema")
        print('-' * 40)
        prodex = str(input('Digite o nome do produto: '))
        selecao = f"""SELECT produto FROM Produtos WHERE produto = '{prodex}' """
        cursor.execute(selecao)
        linhas = cursor.fetchall()
        cursor.commit()

        for linha in linhas:
            varprod_ex = linha[0]
        varprod_ex_str = str(varprod_ex)
        if (prodex == varprod_ex_str):
            comando = f"""DELETE FROM Produtos WHERE produto = '{varprod_ex_str}'"""
            print(comando)
            cursor.execute(comando)
            cursor.commit()

    # excluir cliente
    elif (opcao == 8):
        print('-' * 40)
        print("Digite um cliente cadastrado no sistema")
        print('-' * 40)
        cliex = str(input('Digite o nome do cliente: '))
        selecao = f"""select cliente from Clientes WHERE cliente = '{cliex}'"""
        cursor.execute(selecao)
        linhas = cursor.fetchall()
        cursor.commit()

        for linha in linhas:
            varcli_ex = linha[0]
        varcli_ex_str = str(varcli_ex)
        if (cliex == varcli_ex_str):
            comando = f"""DELETE FROM Clientes WHERE cliente = '{varcli_ex_str}'"""
            print(comando)
            cursor.execute(comando)
            cursor.commit()

    # finalizar produto
    elif (opcao == 9):
        break