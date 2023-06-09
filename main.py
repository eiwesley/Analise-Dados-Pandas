import pandas as pd

# pd.set_option('max_columns', None)
vendas_df = pd.read_csv(r'src/Contoso - Vendas  - 2017.csv', sep=';')
clientes_df = pd.read_csv(r'src/Contoso - Clientes.csv', sep=';')
produtos_df = pd.read_csv(r'src/Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'src/Contoso - Lojas.csv', sep=';')
promocoes_df = pd.read_csv(r'src/Contoso - Promocoes.csv', sep=';')

# clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)
# print(clientes_df)

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Categoria']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendas_df)