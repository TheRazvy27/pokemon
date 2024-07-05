class antrenor:
    def __init__(self, nume, pokemoni):
        self.nume = nume
        self.pokemoni = pokemoni

    def alege_pokemon(self):
        return self.pokemoni[0]

    def are_pokemoni_vii(self):    
        if self.pokemoni:
            return True
        return False

    def test():
        pass