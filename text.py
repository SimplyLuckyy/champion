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

def ending(player):
    time.sleep(1)
    print("Placeholder for ending")