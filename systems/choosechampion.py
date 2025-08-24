from player.playerinfo import Player
from text import *

def choose_champion(champion):

    player_temp = champion

    print("""Who is your champion?\n
- Warrior
- Rogue
- Mage\n""")
    champion_class = input("> ").lower()
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
    if input("> ").lower() == "y":
        print(f"\nYou are the {player_temp.champion}. At any time you may type 'stats' to view your stats.\n")
    else:
        choose_champion(player_temp)
    return player_temp