import pandas as pd

# vendas_df = pd.read_csv('src/Contoso - Cadastro Produtos.csv')
vendas_df = pd.read_csv('src/Contoso - Vendas  - 2017.csv', sep=';')

# print(vendas_df)
# print(vendas_df['ID Cliente'])
# print(vendas_df[:3])
# print(vendas_df[['Numero da Venda', 'Data da Venda', 'ID Produto']])

# vendas_df.info()

# lista_clientes = vendas_df['ID Cliente']
# print(lista_clientes)

# produtos_quantidade = vendas_df[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
# print(produtos_quantidade)