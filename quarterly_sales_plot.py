import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Le o arquivo "CSV" para base de dados
df = pd.read_csv('VendasTrimestrais.csv', header=None, names=['Trimestre', 'Ano', 'Categoria', 'TotalVendas'])

# Cria nova coluna com uma string que concatena ano e trimestre
df['Ano-Trimestre'] = df['Ano'].astype(str) + '-Q' + df['Trimestre'].astype(str)

# Agrupa os dados por trimestre e ano e soma as vendas
df_grouped = df.groupby('Ano-Trimestre')['TotalVendas'].sum().reset_index()

# Define a nova coluna como indice do DataFrame para garantir ordenamento
df_grouped.set_index('Ano-Trimestre', inplace=True)

# Gera o gráfico das vendas trimestrais
fig, ax = plt.subplots()
ax.bar(range(len(df_grouped)), df_grouped['TotalVendas'])
ax.set_xticks(range(len(df_grouped)))
ax.set_xticklabels(df_grouped.index, rotation=45, fontsize=8)
ax.set_xlabel('Ano - Trimestre')
plt.title('Total de Vendas')

# Modifica a escala de valores para milhões
formatter = ticker.FuncFormatter(lambda x, pos: 'R${:.0f} Mi'.format(x / 1000000))
ax.yaxis.set_major_formatter(formatter)

# Adicionar as grades
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.4)
ax.xaxis.grid(False)

# Salva e mostra o grafico gerado
plt.savefig('./Total_de_vendas_trimestrais.jpeg', format='jpeg')
plt.show()
