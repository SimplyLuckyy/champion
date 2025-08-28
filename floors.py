import time
from actors.enemy import *
from systems.combat import battle, next_room
from text import view_stats

def combat1(player):
    enemy = Skeleton()
    time.sleep(1)
    print(f"A {enemy.name} has appeared!\n")
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

def combat2(player):
    time.sleep(1)
    enemy = Spider()
    time.sleep(1)
    print(f"A {enemy.name} has appeared!\n")
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

# Allow Keen Eye do give extra damage
def combat3(player):
    time.sleep(1)
    enemy = Bat()
    time.sleep(1)
    print(f"A {enemy.name} has appeared!\n")
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

def social1(player):
    time.sleep(1)
    print("This is social1")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")

def social2(player):
    time.sleep(1)
    print("This is social2")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")

def social3(player):
    time.sleep(1)
    print("This is social3")
    time.sleep(1)
    if player.keeneye:
        print("Player has Keen Eye")

def loot1(player):
    time.sleep(1)
    print("This is loot1")


def loot2(player):
    time.sleep(1)
    print("This is loot2")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")

def loot3(player):
    time.sleep(1)
    print("This is loot3")
    time.sleep(1)
    time.sleep(1)
    if player.keeneye:
        print("Player has Keen Eye")

def rest_room(player):
    time.sleep(1)
    print("This is rest")


def boss_room(player):
    time.sleep(1)
    print("This is boss")