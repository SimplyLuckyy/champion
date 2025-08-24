import time
from text import *
from player.playerinfo import choose_champion
from systems.roomgen import *



def main ():
    

    floor_count = 1
    

    introduction()
    time.sleep(1)
    player = choose_champion(None)
    if floor_count == 1:
        first_floor_intro()
    else:
        print("You descend to the next floor...\n")
    
    room_gen(floor_count)
    

if __name__ == "__main__":
    main()