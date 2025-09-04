class Player:
    def __init__(self):
        self.name = None
        self.health = 100
        self.energy = 100
        self.gold = 20
        self.potions = 0
        self.attack = 5
        self.defense = 0
        self.energyname = "Stamina"
        self.keeneye = False
        self.arcaneknowledge = False
        # self.fightingspirit = False --- Might include?
        self.items = []

class Warrior(Player):
    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.attack = 10
        self.defense = 5

class Rogue(Player):
    def __init__(self):
        super().__init__()
        self.name = "Rogue"
        self.defense = 5
        self.keeneye = True

class Mage(Player):
    def __init__(self):
        super().__init__()
        self.name = "Mage"
        self.attack = 10
        self.energyname = "Mana"
        self.arcaneknowledge = True
    
class Debug(Player):
    def __init__(self):
        super().__init__()
        self.name = "Developer"
        self.attack = 30
        self.defense = 30
        self.keeneye = True
        self.arcaneknowledge = True



