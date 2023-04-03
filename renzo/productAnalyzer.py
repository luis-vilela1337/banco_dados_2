from database import Database
from datetime import datetime
from writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self):
        self.db = Database("mercado", "compras")

    def total_vendas_por_dia(self, data):
        data_inicio = datetime.strptime(data, "%Y-%m-%d")
        data_fim = data_inicio.replace(hour=23, minute=59, second=59)
        pipeline = [
            {"$match": {"data_compra": {"$gte": data_inicio, "$lte": data_fim}}},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": 1}}},
            {"$project": {"data_compra": "$_id", "total_vendas": 1, "_id": 0}},
            {"$sort": {"data_compra": 1}}
        ]
        result =  self.db.collection.aggregate(pipeline)
        writeAJson(result, 'total_de_vendas')

    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$project": {"produto": "$_id", "total_vendido": 1, "_id": 0}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson(result, 'produto_mais_vendido')

    def maior_compra_individual(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_compra": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$lookup": {"from": "clientes", "localField": "_id", "foreignField": "id", "as": "cliente"}},
            {"$unwind": "$cliente"},
            {"$project": {"cliente": "$cliente.nome", "total_compra": 1, "_id": 0}},
            {"$sort": {"total_compra": -1}},
            {"$limit": 1}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson(result, 'maior_compra_individual')

    def produtos_frequentemente_vendidos(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 1}}},
            {"$project": {"produto": "$produtos.descricao", "quantidade_vendida": "$produtos.quantidade", "_id": 0}},
            {"$sort": {"produto": 1}}
        ]
        result = self.db.collection.aggregate(pipeline)
        writeAJson(result, 'produto_frequentemente_vendidos')