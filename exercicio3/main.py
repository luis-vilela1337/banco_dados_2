from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

pokedex = Pokedex(database_name="pokedex", collection_name="pokemons")

pokedex.get_all_pokemons()
pokedex.get_pokemon_by_name(name = 'Pikachu')
pokedex.get_pokemon_by_id(pokemon_id = 149)
pokedex.get_pokemon_by_type(pokemon_type = ["Grass", "Poison"])
pokedex.get_pokemon_by_weakness(weakness = ["Psychic", "Ice"])