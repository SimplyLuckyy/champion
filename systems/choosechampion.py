from actors.player import Player
from text import *

def choose_champion(champion):

    player_temp = champion
    time.sleep(1)
    print("""Who is your Champion?\n
1. Warrior
2. Rogue
3. Mage\n""")
    champion_class = input("> ")
    print("")
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
    
    print("Confirm your Champion? [y/n]\n")
    choice = input("> ").lower()
    print("")
    if choice == "y":
        return player_temp
    elif choice == "n":
        return choose_champion(player_temp)
    else:
        print("Invalid Choice\n")
        return choose_champion(player_temp)
    