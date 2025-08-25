import time
from actors.enemy import *
from text import *
from systems.roomgen import *
from systems.choosechampion import *
from systems.combat import *

# reminder to put "> " at the start of all player inputs for clarity

def main():
    

    floor_count = 1
    room_list = [combat1, combat2, combat3,
                social1, social2, social3, 
                loot1, loot2, loot3]
    

    # introduction()
    time.sleep(1)
    player = choose_champion(None)

    enemy_temp = Skeleton()

    if floor_count == 1:
        first_floor_intro()
    else:
        print("You descend to the next floor...\n")
    
    dodamage(player, enemy_temp)

    '''
    room_gen(floor_count, room_list, player)

    # temp replay
    time.sleep(1)
    print("play again? [y/n]")
    if input("> ").lower() == "y":
        main()
    '''
# write game over & replay function (Take stuff from main put it in a game() funct. When game ends (when player dies) ask if want to continue. Runs game recursively)

if __name__ == "__main__":
    main()