class Player:
    def __init__(self):
        self.name = None
        self.health = 100
        self.energy = 100
        self.gold = 10
        self.potions = 0
        self.attack = 10
        self.defense = 2
        self.energyname = "Stamina"
        self.weaponname = "Stick"
        self.keeneye = False
        self.arcaneknowledge = False
        # self.fightingspirit = False --- Might include?
        self.items = []

class Warrior(Player):
    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.health = 150
        self.weaponname = "Sword"
        self.attack = 15
        self.defense = 5

class Rogue(Player):
    def __init__(self):
        super().__init__()
        self.name = "Rogue"
        self.energy = 150
        self.weaponname = "Bow"
        self.defense = 8
        self.keeneye = True

class Mage(Player):
    def __init__(self):
        super().__init__()
        self.name = "Mage"
        self.energy = 150
        self.weaponname = "Staff"
        self.attack = 15
        self.energyname = "Mana"
        self.arcaneknowledge = True
    
class Debug(Player):
    def __init__(self):
        super().__init__()
        self.name = "Developer"
        self.health = 300
        self.energy = 300
        self.gold = 30
        self.potions = 10
        self.attack = 40
        self.defense = 40
        self.keeneye = True
        self.arcaneknowledge = True



