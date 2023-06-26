from pymongo import MongoClient
from bson.objectid import ObjectId


class FuncionarioModel:
    def __init__(self, database):
        self.db = database

    def create_funcionario(self, nome: str, cargo: str, salario: float):
        try:
            funcionario = {"nome": nome, "cargo": cargo, "salario": salario}
            res = self.db.collection.insert_one(funcionario)
            print(f"Funcionário criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o funcionário: {e}")
            return None

    def read_funcionario_by_id(self, id: str):
        try:
            funcionario = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Funcionário encontrado: {funcionario}")
            return funcionario
        except Exception as e:
            print(f"Ocorreu um erro ao ler o funcionário: {e}")
            return None

    def update_funcionario(self, id: str, nome: str = None, cargo: str = None, salario: float = None):
        try:
            query = {"_id": ObjectId(id)}
            update = {"$set": {}}
            if nome:
                update["$set"]["nome"] = nome
            if cargo:
                update["$set"]["cargo"] = cargo
            if salario:
                update["$set"]["salario"] = salario

            res = self.db.collection.update_one(query, update)
            print(f"Funcionário atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o funcionário: {e}")
            return None

    def delete_funcionario(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Funcionário deletado: {res.deleted_count} documento(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o funcionário: {e}")
            return None