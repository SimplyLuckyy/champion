import time
from text import *

class Player:
    def __init__(self):
        self.champion = None
        self.health = 100
        self.energy = 100
        self.gold = 20
        self.potions = 0
        self.attack = 5
        self.defense = 5
        self.energyname = "Stamina"
        self.keeneye = False
        self.arcaneknowledge = False

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
        self.keeneye = True

class Mage(Player):
    def __init__(self):
        super().__init__()
        self.champion = "Mage"
        self.attack = 10
        self.energyname = "Mana"
        self.arcaneknowledge = True
    
class Debug(Player):
    def __init__(self):
        super().__init__()
        self.champion = "Developer"
        self.attack = 30
        self.defense = 30
        self.keeneye = True
        self.arcaneknowledge = True



def choose_champion(champion):

    player_temp = champion

    print("""Who is your champion?\n
- Warrior
- Rogue
- Mage\n""")
    champion_class = input().lower()
    if champion_class == "warrior":
        warrior_description()
        time.sleep(1)
        player_temp = Warrior()
    elif champion_class == "rogue":
        rogue_description()
        time.sleep(1)
        player_temp = Rogue()
    elif champion_class == "mage":
        mage_description()
        time.sleep(1)
        player_temp = Mage()
    elif champion_class == "/godmode":
        debug_description()
        time.sleep(1)
        player_temp = Debug()
    else:
        print("Invalid Champion\n")
        time.sleep(1)
        choose_champion(player_temp)
    
    print("Confirm your champion? [y/n]\n")
    if input().lower() == "y":
        print(f"You are the {player_temp.champion}. At any time you may type 'stats' to view your stats.\n")
    else:
        choose_champion(player_temp)
    return player_temp