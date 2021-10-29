from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return 'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = [f"Pokemon Trainer {self.name}", f'Pokemon count {len(self.pokemons)}']
        for pokemon in self.pokemons:
            data.append(f'- {pokemon.pokemon_details()}')
        return '\n'.join(data)
