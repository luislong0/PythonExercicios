#filtro de tabela

import pandas as pd

tabela = pd.read_excel("TabelaOpenPy.xlsx")
mascara = tabela["Tipo"] == "Produto"
tabela2 = tabela[mascara]
print(tabela2)

# tabela2.to_excel("excel4.xlsx")