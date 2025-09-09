from actors.player import Player
from text import *

def choose_champion(champion):

    player_temp = champion

    print("""Who is your champion?\n
1. Warrior
2. Rogue
3. Mage\n""")
    champion_class = input("> ")
    match champion_class:
        case "1":
            warrior_description()
            time.sleep(1)
            player_temp = Warrior()
        case "2":
            rogue_description()
            time.sleep(1)
            player_temp = Rogue()
        case "3":
            mage_description()
            time.sleep(1)
            player_temp = Mage()
        case "/godmode":
            debug_description()
            time.sleep(1)
            player_temp = Debug()
        case _:
            print("Invalid Champion\n")
            time.sleep(1)
            return choose_champion(player_temp)
    
    print("Confirm your champion? [y/n]\n")
    choice = input("> ").lower()
    print("")
    if choice == "y":
        print(f"You are the {player_temp.name}. At any time you may type 'stats' to view your stats.\n")
        return player_temp
    elif choice == "n":
        return choose_champion(player_temp)
    else:
        print("Invalid Choice\n")
        return choose_champion(player_temp)
    