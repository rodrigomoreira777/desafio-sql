CREATE TABLE VendasTrimestrais (
Trimestre INT,
Ano INT,
Categoria VARCHAR(50),
TotalVendas DECIMAL(10,2)
)

INSERT INTO VendasTrimestrais
SELECT
DATEPART(QUARTER, CONVERT(DATE, [Data_da_Venda], 103)) AS Trimestre,
YEAR(CONVERT(DATE, [Data_da_Venda], 103)) AS Ano,
Categoria,
SUM(CAST(REPLACE([Valor], 'R$ ', '') AS DECIMAL(10,2))) AS TotalVendas
FROM dbo.db_teste
GROUP BY DATEPART(QUARTER, CONVERT(DATE, [Data_da_Venda], 103)),
YEAR(CONVERT(DATE, [Data_da_Venda], 103)),
Categoria
