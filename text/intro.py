import time
from player.playerinfo import *

boarder = "\n" + "=" * 20 + "\n"

def choose_champion():

    # Transform into a recursive choose Champion function
    print("""Who is your champion?\n
- Warrior
- Rogue
- Mage\n""")
    champion_class = input().title()
    if champion_class == "Warrior":
        print("WARRIOR DESCRIPTION")
        time.sleep(1)
        player_temp = Warrior()
    elif champion_class == "Rogue":
        print("ROGUE DESCRIPTION")
        time.sleep(1)
        player_temp = Rogue()

    elif champion_class == "Mage":
        print("MAGE DESCRIPTION")
        time.sleep(1)
        player_temp = Mage()
    else:
        print("invalid champion")
        time.sleep(1)
        choose_champion()
    
    time.sleep(1)
    print("Confirm your champion? [y/n]\n")
    if input().lower() == "y":
        print(f"You are the {champion_class}.")
    else:
        choose_champion()
    return player_temp




    