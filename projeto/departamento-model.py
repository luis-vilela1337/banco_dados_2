from pymongo import MongoClient
from bson.objectid import ObjectId

class DepartamentoModel:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.departamentos

    def create_departamento(self, nome: str, localizacao: str):
        try:
            departamento = {"nome": nome, "localizacao": localizacao, "funcionarios": []}
            res = self.collection.insert_one(departamento)
            print(f"Departamento criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o departamento: {e}")
            return None

    def read_departamento_by_id(self, id: str):
        try:
            departamento = self.collection.find_one({"_id": ObjectId(id)})
            print(f"Departamento encontrado: {departamento}")
            return departamento
        except Exception as e:
            print(f"Ocorreu um erro ao ler o departamento: {e}")
            return None

    def update_departamento(self, id: str, nome: str = None, localizacao: str = None):
        try:
            query = {"_id": ObjectId(id)}
            update = {"$set": {}}
            if nome:
                update["$set"]["nome"] = nome
            if localizacao:
                update["$set"]["localizacao"] = localizacao

            res = self.collection.update_one(query, update)
            print(f"Departamento atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o departamento: {e}")
            return None

    def delete_departamento(self, id: str):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"Departamento deletado: {res.deleted_count} documento(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o departamento: {e}")
            return None
