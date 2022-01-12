class Pokemon:
    def __init__(self, p):
        self.pokemon = p
        self.pokemon_type = "Needs to be set"
        self.pokemon_weakness = "Needs to be set"
    def kind(self):
        return self.pokemon_type
    def weakness(self):
        return self.pokemon_weakness
    def what_am_i(self):
        
        print("I am a Pokemon.")
        

class Pikachu(Pokemon):
    def __init__(self, p = "Pikachu"):
        super().__init__(p)
        self.pokemon_type = "Electric"
        self.pokemon_weakness = "Ground"
    def what_am_i(self):
        print("I am a Pokemon.")
        print(f"I am {self.pokemon}.")

class Charmander(Pokemon):
    def __init__(self, p = "Charmander"):
        super().__init__(p)
        self.pokemon_type = "Fire"
        self.pokemon_weakness = "Water, Ground and Rock"
    def what_am_i(self):
        print("I am a Pokemon.")
        print(f"I am {self.pokemon}.")  

pk1 = Pikachu()
print("Pokemon:", pk1.pokemon)
print("Type:", pk1.kind())
print("Weakness:", pk1.weakness())
pk1.what_am_i()
print("========================")
c1 = Charmander()
print("Pokemon:", c1.pokemon)
print("Type:", c1.kind())
print("Weakness:", c1.weakness())
c1.what_am_i()