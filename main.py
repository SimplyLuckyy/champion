import time
from actors.enemy import *
from text import *
from floors import *
from systems.roomgen import *
from systems.choosechampion import *
from systems.combat import *

# reminder to put "> " at the start of all player inputs for clarity

def main():
    
        floor_count = 1
        room_list = [combat1, combat2, combat3,
                    social1, social2, social3, 
                    loot1, loot2, loot3]
        
        introduction()
        time.sleep(1)
        player = choose_champion(None)

        if floor_count == 1:
            first_floor_intro()
        else:
            print("You descend to the next floor...\n")
        room_gen(floor_count, room_list, player)
        time.sleep(1)
        print(boarder)
        playagain()

def playagain():
    
    print("Play Again? [y/n]\n")
    choice = input("> ").lower()
    if choice == "y":
        main()
    elif choice == "n":
        exit()
    else:
        print("Ivalid Choice\n")
        playagain()

if __name__ == "__main__":
    main()