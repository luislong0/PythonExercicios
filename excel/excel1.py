#pandas
import pandas as pd

tabela = pd.read_excel("treino.xlsx")
print(tabela)

# atualizar o multiplicador
tabela.loc[tabela["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5

# fazer a conta do Preço base reais
tabela["Preço base reais"] = tabela["Multiplicador Imposto"] * tabela["Preço base original"]

#criar arquivo excel
tabela.to_excel("TabelaPandas.xlsx")