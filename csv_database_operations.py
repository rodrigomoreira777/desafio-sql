import pandas as pd
import sys


def formata_para_string(numero):
    """
    Função definida para formatar um float, separando as casas decimais por "," e "." para separar as milhares.
    :param numero: O float a ser formatado, exemplo "29964.48".
    :return: O número formatado como uma string " R$ 29.964,48 ".
    """
    # Arrendonda o valor, converte o número para string e separa a parte inteira da parte decimal
    numero = round(numero, 2)
    numero_str = str(numero)
    partes = numero_str.split(".")
    inteira = partes[0]
    decimal = partes[1] if len(partes) > 1 else ""

    # Adiciona "." a cada grupo de 3 dígitos da parte inteira, ou seja, acrescenta uma representação milhar.
    inteira_formatada = ""
    for i in range(len(inteira)):
        inteira_formatada += inteira[i]
        if (len(inteira) - i - 1) % 3 == 0 and i != len(inteira) - 1:
            inteira_formatada += "."

    # Concatena a parte inteira e a parte decimal com utilizando a ","
    if decimal:
        numero_formatado = inteira_formatada + "," + decimal
    else:
        numero_formatado = inteira_formatada

    return numero_formatado


# Le do arquivo "csv" para uma base de dados
df = pd.read_csv('DB_Teste.csv', delimiter=';')

# Remoção de caracteres da string "Valor". Ou seja, remove os caracteres " R$ ",  "." e substitui "," por "." em decimal
df['Valor'] = df['Valor'].str.replace('R', '').str.replace('$', '').str.replace('.', '').str.replace(' ', '')
df['Valor'] = df['Valor'].str.replace(',', '.')

# Converte a coluna "Valor" para float
df['Valor'] = df['Valor'].astype(float)

# Cria a tabela auxiliar com a soma de vendas de cada vendedor
vendas_por_vendedor = df.groupby('Vendedor')['Valor'].sum().reset_index().sort_values('Valor', ascending=False)

# Formatação dos valores para imprimir com separação de milhar por "." e casas decimais por ","
vendas_por_vendedor['Valor'] = vendas_por_vendedor['Valor'].apply(
    lambda x: '{:,.2f}'.format(x).replace(',', 'v').replace('.', ',').replace('v', '.'))

# Salva tabela auxiliar em um arquivo CSV
vendas_por_vendedor.to_csv('VendasPorVendedor.csv', index=False)

# Obtem em variaveis o cliente com a venda de maior valor e o respectivo resultado
cliente_maior_valor = df.iloc[df['Valor'].idxmax()]['Cliente']
valor_maior_venda = df.iloc[df['Valor'].idxmax()]['Valor']

# Obtem em variaveis o cliente com a venda de menor valor e o respectivo resultado
cliente_menor_valor = df.iloc[df['Valor'].idxmin()]['Cliente']
valor_menor_venda = df.iloc[df['Valor'].idxmin()]['Valor']

# Calcula o valor medio para cada tipo de venda
servicos_mean = df[df['Tipo'] == 'Serviços']['Valor'].mean()
licenciamento_mean = df[df['Tipo'] == 'Licenciamento']['Valor'].mean()
produtos_mean = df[df['Tipo'] == 'Produtos']['Valor'].mean()


# Sabe-se que cada linha representa uma venda, assim, conta-se o numero de vezes que cada cliente apareceu
vendas_por_cliente = df.groupby('Cliente').size().reset_index(name='Quantidade de Vendas')

# Ordena em ordem decrescente, o de maior vendas de vendas realizadas para o de menor vendas realizadas
vendas_por_cliente = vendas_por_cliente.sort_values(by='Quantidade de Vendas', ascending=False)

# Configura as opções da biblioteca "pandas" para exibir todas as colunas, as linhas e omite o indice das linhas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Abre o arquivo para escrita dos valores a serem impressos
with open('output.txt', 'w') as f:
    # Redireciona a os prints do console para o arquivo "output.txt"
    sys.stdout = f

    # Imprime o resultado do cliente de maior e menor valor de venda
    print(
        f'O cliente com a venda de maior valor foi: {cliente_maior_valor} com o valor de R$ '
        f'{formata_para_string(valor_maior_venda)}')
    print(
        f'O cliente com a venda de menor valor foi: {cliente_menor_valor} com o valor de R$ '
        f'{formata_para_string(valor_menor_venda)}\n')

    # impreme os valores medios por Tipo de venda (Serviços, Licenciamento, Produtos)
    print(f'Valor médio de Serviços: R$ {formata_para_string(servicos_mean)}')
    print(f'Valor médio de Licenciamento: R$ {formata_para_string(licenciamento_mean)}')
    print(f'Valor médio de Produtos: R$ {formata_para_string(licenciamento_mean)}\n')
    print(vendas_por_cliente.to_string(index=False))

    # Restaura a saada para o console no lugar do arquivo
    sys.stdout = sys.__stdout__

# Restaura as configurações originais da biblioteca "pandas"
pd.reset_option('display.max_columns')
pd.reset_option('display.max_rows')
