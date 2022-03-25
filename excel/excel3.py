import pandas as pd

# lendo tabelas
tabela1 = pd.read_excel("treino.xlsx")
tabela2 = pd.read_excel("produto.xlsx")

# juntando tabelas
tabelas = pd.concat([tabela1, tabela2])

# print (tabelas["Tipo"])

# equações com tabelas
conta = tabela1.groupby(["Tipo"]).sum()
maximo = tabela1["Preço base reais"].max()
minimo = tabela1["Preço base reais"].min()

# printando tabelas
print (conta)
print()
print (maximo)
print()
print (minimo)

#pegar uma parte da tabela
relatorio_lindo = tabela1.loc[:, "Tipo":"Preço base reais"]
print(relatorio_lindo)


