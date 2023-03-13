from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database_name, collection_name):
        self.db = Database(database_name, collection_name)

    def get_all_pokemons(self):
        response = list(self.db.collection.find())
        writeAJson(response, "get_all_pokemons")

    def get_pokemon_by_name(self, name):
        response =  self.db.collection.find_one({'name': name})
        writeAJson(response, "get_pokemon_by_name")

    def get_pokemon_by_id(self, pokemon_id):
        response =  self.db.collection.find_one({'id': pokemon_id})
        writeAJson(response, "get_pokemon_by_id")

    def get_pokemon_by_type(self, pokemon_type):
        response =  list(self.db.collection.find({'type': {"$in": pokemon_type}}))
        writeAJson(response, "get_pokemon_by_type")

    def get_pokemon_by_weakness(self, weakness):
        response =  list(self.db.collection.find({'weaknesses': {"$all": weakness}}))
        writeAJson(response, "get_pokemon_by_weakness")

