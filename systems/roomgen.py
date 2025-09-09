from text import boarder, ending
from floors import *
import time
import random

def room_gen(floor_count, room_list, player):
    boss_floor = 5 + 1
    limit_list = [social1, social2, social3, 
                loot1, loot2, loot3]

    if floor_count == boss_floor:
        print(f"{boarder}\n")
        boss_room(player)
    elif floor_count % 5 == 0:
        print(boarder)
        print(f"FLOOR {floor_count}\n")
        rest_room(player)
    else:
        print(boarder)
        print(f"FLOOR {floor_count}\n")
        room_type = random.randint(0, len(room_list) -1)
        room_list[room_type](player)
    
        if room_list[room_type] in limit_list:
            del room_list[room_type]
    
    if floor_count != boss_floor: 
        floor_count += 1
        time.sleep(1)
        print("You descend to the next floor...")
        time.sleep(1)
        room_gen(floor_count, room_list, player)
    else:
        print(f"{boarder}\n")
        ending(player)