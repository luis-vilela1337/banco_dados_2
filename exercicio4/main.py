from database import Database
from writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

pa = ProductAnalyzer()
pa.total_vendas_por_dia('2022-03-14')
pa.produto_mais_vendido()
pa.maior_compra_individual()
pa.produtos_frequentemente_vendidos()
