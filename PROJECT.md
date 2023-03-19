# Resolução do desafio - Estágio Desenvolvedor SQL

Esse arquivo tem como objetivo explicar como executar o projeto desenvolvido e apresentar detalhes dos códigos que foram implementados.

## Lista de arquivos do diretório:

- **DB_Teste.csv**: arquivo contendo as informações fornecidas para realizar o desafio;
- **DiagramaEntidadeRelacionamento.jpeg**: imagem do modelo de relacionamento, com as categorias apresentads nos campos do arquivo CSV;
- **PROJECT.md**: arquivo de instruções para executar o projeto.
- **README.md**: arquivo fornecido para instruir o participante como deve ser realizado o desafio e o que entregar;
- **Total_de_vendas_trimestrais.jpeg**: gráfico do histórico trimestral de vendas;
- **VendasPorVendedor.csv**: tabela auxiliar que sumariza o valor vendido por cada vendedor, ordenando do maior para o menor;
- **VendasTrimestrais.csv**: tabela que avalia trimestralmente o resultado de vendas;
- **csv_database_operations.py**: arquivo em linguagem Python que realiza as tarefas solicitadas na primeira parte do desafio;
- **output.txt**: arquivo texto que armazena as saídas do console quando executado o arquivo "csv_database_operations.py";
- **quarterly_sales_plot.py**: arquivo em linguagem Python que quando executado realiza a tarefa de gerar o gráfico de histórico trimestral de vendas;
- **query_resultado_vendas_trimestral.sql**: query que gera a tabela que avalia trimestralmente o resultado de vendas;
- **sales_customers_2020.sql**: query que lista todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020;
- **sales_team.sql**: query que lista a equipe de cada vendedor.

## Execução do desafio

### Primeira parte

Inicialmente, para resolução da primeira parte do desafio, foi criado um arquivo em linguagem Python com o nome "csv_database_operations.py". Esse é o primeiro arquivo que deve ser executado.

No começo desse arquivo, para auxiliar na resolução do desafio, foram importadas as bibliotecas pandas para trabalhar na análise dos dados e sys para salvar as saídas do terminal em um arquivo de texto.

Na sequência, no arquivo Python criado, foi definida a função "formata_para_string", que recebe como entrada um número float, arredonda esse valor e o formata como uma string, na forma de representação de moeda (reais). Dessa forma, caso a função, por exemplo, receba o valor "29964.48" como entrada, o retorno da função será o valor "R$ 29.964,48". Essa função é útil no decorrer do código para representar, de uma forma simplificada, os dados numéricos de uma forma mais amigável.

Posteriormente, nesse mesmo arquivo Python, foi utilizado o método "read_csv()" para ler e armazenar a base de dados em formato "csv" em uma variável, que será um objeto da classe "pandas.core.frame.DataFrame". Em seguida, para que se possa trabalhar com a coluna "Valor" na forma numérica, foram removidos os caracteres " R$ ", ".", substituído o "," por "." para as casas decimais e convertidos os valores dessa coluna para o tipo float.

Seguindo no código, foi criado um novo dataframe com o nome "vendas_por_vendedor" para auxiliar na soma das vendas de cada vendedor. Em seguida, os valores do campo "Valor" foram convertidos para a forma de moeda e uma nova tabela foi salva em um arquivo "csv" com o nome "VendasPorVendedor.csv". Finalizando a primeira etapa da primeira parte do desafio, ou seja, de construir uma tabela auxiliar que sumariza o valor vendido por cada vendedor, ordenando do maior para o menor;

Depois, nas linhas de código desse primeiro arquivo a ser executado, foram salvos em variáveis o cliente com a venda de maior valor, o resultado do maior valor de venda, o cliente com a venda de menor valor e o resultado do menor valor de venda. Em seguida, também foram salvos em variáveis o valor médio para cada tipo de venda (Serviços, Licenciamento, Produtos).

No restante do código, sabendo que cada linha representa uma venda, contou-se o número de vezes que cada cliente apareceu para se obter as vendas por cliente.

Posteriormente, modificou-se os parâmetros padrão da biblioteca "pandas" para exibir todas as linhas dos dataframes impressos no console e omitir os índices.

Por fim, foram utilizados comandos para criar o arquivo de texto "output.txt" e salvar, em sequência, as saídas solicitadas para serem impressas. O arquivo "output.txt" contém as respostas para a impressão que identifica qual foi o cliente responsável pela venda com maior valor e com menor valor, valor médio por tipo de venda (Serviços, Licenciamento, Produtos) e o número de vendas realizadas por cliente.

### Segunda parte

Para a solução da segunda parte do desafio, foi criado o arquivo "DiagramaEntidadeRelacionamento.jpeg", que apresenta, na forma de imagem, o modelo de relacionamento com as categorias utilizadas em todos os campos do arquivo "CSV".

Posteriormente, utilizando o Microsoft SQL Server, a base de dados do arquivo "DB_Teste.csv" foi importada como tabela, utilizando o caractere ";" para identificar a separação das colunas.

Em seguida, na nova base de dados, foi criada a query "sales_customers_2020.sql". Essa query é responsável por listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020.

Além disso, foi criada a nova query "sales_team.sql" para listar a equipe de cada vendedor.

Para a última parte do desafio, foi criada a query "query_resultado_vendas_trimestral.sql", que deve ser executada para criar uma nova tabela com as vendas trimestrais. Essa nova tabela deve ser exportada, no formato "csv", e está salva no repositório com o nome "VendasTrimestrais.csv".

Para finalizar o desafio, foi criado um segundo código em linguagem Python, com o nome "quarterly_sales_plot.py". Esse arquivo, ao ser executado, utiliza os dados da tabela de vendas trimestrais gerada anteriormente ("VendasTrimestrais.csv") para criar um gráfico de barras que avalia trimestralmente o resultado de vendas. Esse código também utiliza a biblioteca "pandas" para acessar e realizar operações nos dados tabelados e a biblioteca "matplotlib" para gerar o gráfico e configurar seus parâmetros visuais. Ao executar esse arquivo, é gerado o gráfico de análise trimestral, identificado no diretório como o arquivo "Total_de_vendas_trimestrais.jpeg".

