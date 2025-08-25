import time
from actors.player import *

boarder = "=" * 20

def warrior_description():
    time.sleep(1)
    print("\nPlaceholder for Warrior\n")

def rogue_description():
    time.sleep(1)
    print("\nPlaceholder for Rogue\n")

def mage_description():
    time.sleep(1)
    print("\nPlaceholder for Mage\n")

def debug_description():
    time.sleep(1)
    print("\nPlaceholder for Developer\n")

def view_stats(player):
    print(f"""
{boarder}
STATS

Class: {player.name}
Health: {player.health}
{player.energyname}: {player.energy}
Gold: {player.gold}
Potions: {player.potions}
Attack: {player.attack}
Defense: {player.defense}""")
    if len(player.items) > 0:
        print(f"Items: {player.items}")
print(f"\n{boarder}")


def introduction():
    time.sleep(1)
    print("\nPlaceholder for intro\n")

def first_floor_intro():
    time.sleep(1)
    print("Placeholder for First Floor\n")


def combat1(player):
    time.sleep(1)
    print("This is combat1")

def combat2(player):
    time.sleep(1)
    print("This is combat2")

def combat3(player):
    time.sleep(1)
    print("This is combat3")
    time.sleep(1)
    if player.keeneye:
        print("Player has Keen Eye")

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
        print("Play has Arcane Knowledge")

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

def ending(player):
    time.sleep(1)
    print("Placeholder for ending")