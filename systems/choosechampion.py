from actors.player import Player
from text import *

def choose_champion(champion):

    player_temp = champion

    print("""Who is your champion?\n
1. Warrior
2. Rogue
3. Mage\n""")
    champion_class = input("> ")
    if champion_class == "1":
        warrior_description()
        time.sleep(1)
        player_temp = Warrior()
    elif champion_class == "2":
        rogue_description()
        time.sleep(1)
        player_temp = Rogue()
    elif champion_class == "3":
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
        return choose_champion(player_temp)
    
    print("Confirm your champion? [y/n]\n")
    choice = input("> ").lower()
    if choice == "y":
        print(f"\nYou are the {player_temp.name}. At any time you may type 'stats' to view your stats.\n")
    elif choice == "n":
        choose_champion(player_temp)
    else:
        print("Invalid Choice")
        choose_champion(player_temp)
    return player_temp