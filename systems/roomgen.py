from text import combat1, combat2, combat3, loot1, loot2, loot3, social1, social2, social3, rest_room, boss_room, ending
import random

# Implement a way to prevent loot & social encounters from repeating? Or keep as is?

def room_gen(floor_count):
    boss_floor = 10 + 1

    if floor_count == boss_floor:
        boss_room()
    elif floor_count % 5 == 0:
        rest_room()
    else:
        room_list = [[combat1, combat2, combat3],
                    [social1, social2, social3], 
                    [loot1, loot2, loot3]]
        room = random.choice(room_list[random.randint(0,2)])
        room()
        
    
    if floor_count != boss_floor: 
        floor_count += 1
        room_gen(floor_count)
    else:
        ending()