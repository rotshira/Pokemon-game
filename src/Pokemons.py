# from client_python import client

class pokemons:
    num = 0

    def __init__(self, pokemon: dict = {}):
        self.pokemon: dict = pokemon

    def add_pokemon(self,id: int, pos:(), value: float, type: int):
        d = {id: (pos,value, type)}
        self.pokemon.update(d)


