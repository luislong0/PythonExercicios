import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-PMKKLEA\SQLEXPRESS;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

id = 3
cliente = "Lira Python"
produto = "Carro"
data = "25/08/2021"
preco = 5000
quantidade = 1

selecao = f"""select * from Vendas"""

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

# cursor.execute(comando)
cursor.execute(selecao)
linhas = cursor.fetchall()
cursor.commit()

print("\n Mostrando os dados cadastrados")
for linha in linhas:
    print("id_venda:", linha[0])
    print("cliente:", linha[1])
    print("produto:", linha[2])
    print("data_venda:", linha[3])
    print("preco:", linha[4])
    print("quantidade:", linha[5])
    print()


