from pymongo import MongoClient
from bson.objectid import ObjectId


class BookModel:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.collection_name

    def create_book(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            book = {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
            res = self.collection.insert_one(book)
            print(f"Book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating a book: {e}")
            return None

    def read_book_by_id(self, id: str):
        try:
            book = self.collection.find_one({"_id": ObjectId(id)})
            print(f"Book found: {book}")
            return book
        except Exception as e:
            print(f"An error occurred while reading book: {e}")
            return None

    def update_book(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            query = {"_id": ObjectId(id)}
            update = {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}}
            res = self.collection.update_one(query, update)
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating book: {e}")
            return None

    def delete_book(self, id: str):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"Book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting book: {e}")
            return None
