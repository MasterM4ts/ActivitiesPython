#Apresentação#

import pandas as pd

vendas = {'data':['26/06/2023','27/06/2023'],'valor':[15,20],'produto':['feijão','arroz'],'qtde':[15,20]}
print(vendas,'\n')
tabela_vendas = pd.DataFrame(vendas)
print(tabela_vendas)


tabela_vendas = pd.read_excel("Vendas.xlsx")
print(tabela_vendas)

tabela_vendas = pd.read_excel("Vendas.xlsx")
print(tabela_vendas.shape)

tabela_vendas = pd.read_excel("Vendas.xlsx")
print(tabela_vendas.head(4))

tabela_vendas = pd.read_excel("Vendas.xlsx")
print(tabela_vendas.describe())

tabela_vendas = pd.read_excel("Vendas.xlsx")
produtos = tabela_vendas['Produto':'ID Loja']
print(produtos)

tabela_vendas = pd.read_excel("Vendas.xlsx")
print(tabela_vendas.loc[1:2])

tabela_vendas = pd.read_excel("Vendas.xlsx")
print(tabela_vendas.loc[tabela_vendas['ID Loja']=='NOrte Shopping'])

tabela_vendas = pd.read_excel("Vendas.xlsx")
Norte_Shopping = tabela_vendas.loc[tabela_vendas['ID Loja']=='Norte Shopping']
print(Norte_Shopping)