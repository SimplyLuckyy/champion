
class Player:
    def __init__(self):
        self.champion = None
        self.health = 100
        self.energy = 100
        self.gold = 20
        self.attack = 5
        self.defense = 5
        self.energyname = "Stamina"
        self.ability = "None"

class Warrior(Player):
    def __init__(self):
        super().__init__()
        self.champion = "Warrior"
        self.attack = 10
        self.defense = 10

class Rogue(Player):
    def __init__(self):
        super().__init__()
        self.champion = "Rogue"
        self.defense = 10
        self.ability = "Keen Eye"

class Mage(Player):
    def __init__(self):
        super().__init__()
        self.champion = "Mage"
        self.attack = 10
        self.energyname = "Mana"
        self.ability = "Arcane Knowledge"