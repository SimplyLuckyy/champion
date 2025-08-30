import time
from actors.enemy import *
from systems.combat import battle, next_room
from text import view_stats

# todo list:
# Combat Rooms - DONE
# Social Rooms - WIP
# Loot Rooms - WIP

def combat1(player):
    enemy = Skeleton()
    time.sleep(1)
    print(f"A {enemy.name} has appeared!\n")
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

def combat2(player):
    enemy = Spider()
    time.sleep(1)
    print(f"A {enemy.name} has appeared!\n")
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

def combat3(player):
    enemy = Bat()
    time.sleep(1)
    print(f"A {enemy.name} has appeared!\n")
    if player.keeneye:
        print(f"Your Keen Eye alerts you to its weak points.\n{enemy.name}'s defenses reduced!\n")
        enemy.defense -= 3
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

# Potion Merchant + Spellbook
def social1(player):
    time.sleep(1)
    print("This is social1")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")
    next_room(player)

# ??? + elixirs
def social2(player):
    time.sleep(1)
    print("This is social2")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")
    next_room(player)

# Adventurer who attacks you + Explosives
def social3(player):
    time.sleep(1)
    print("This is social3")
    time.sleep(1)
    if player.keeneye:
        print("Player has Keen Eye")
    next_room(player)

# Gold
def loot1(player):
    time.sleep(1)
    print("In the room stands a lone chest.\n What do you do?\n")
    print("1. Approach\n2. Ignore")

    next_room(player)

# Defense Boost + Magic Sheild
def loot2(player):
    time.sleep(1)
    print("This is loot2")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")
    next_room(player)

# Attack Boost + Barbed Arrow
def loot3(player):
    time.sleep(1)
    print("This is loot3")
    time.sleep(1)
    time.sleep(1)
    if player.keeneye:
        print("Player has Keen Eye")
    next_room(player)

# Restore 50% of lost health & energy
def rest_room(player):
    time.sleep(1)
    print("This is rest")
    restore_health = ((100 - player.health) // 2) + 1
    restore_energy = ((100 - player.energy) // 2) + 1
    player.health += restore_health
    player.energy += restore_energy
    next_room(player)


# Auuuuuuughhhhhhh
def boss_room(player):
    time.sleep(1)
    print("This is boss")