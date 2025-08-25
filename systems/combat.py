from text import boarder
from actors.player import Player
from actors.enemy import Enemy
import random
import time

def dodamage(attacker, defender):
    damage_delt = (attacker.attack * 2) - defender.defense
    time.sleep(1)
    print(f"{attacker.name} deals {damage_delt} damage")
    if isinstance(defender, Player) and "Magic Sheild" in defender.items: 
        if not magicsheild(defender): 
            defender.health -= damage_delt
    if isinstance(attacker, Player) and ("Barbed Arrow" in attacker.items or "Spellbook" in attacker.items):
        (using, damage_delt) = combatitem(attacker, damage_delt)
        if using:
            print(damage_delt)
            defender.health -= damage_delt

        
def magicsheild(player):
    print("Would you like to negate damage? [y/n]\n")
    response = input("> ").lower()
    if response == "y":
        time.sleep(1)
        print("Damage Negated!\n")
        player.items.remove("Magic Sheild")
        print("The Magic Sheild shatters...")
        return True
    elif response == "stats":
        print("stats funct placeholder\n")
        return magicsheild(player)
    elif response == "n":
        print("Damge not negated\n")
        return False
    else:
        return magicsheild(player)

def combatitem(player, damage_delt):
    damage_bonus = 5

    if "Barbed Arrow" in player.items:
        print("Would you like to use the Barbed Arrow? [y/n]\n")
        response = input("> ").lower()
        if response == "y":
            time.sleep(1)
            damage_delt += damage_bonus
            print(f"Damage increased to {damage_delt}!\n")
            player.items.remove("Barbed Arrow")
            print("The arrow was used up...")
        elif response == "stats":
            print("stats funct placeholder\n")
            return combatitem(player)
        elif response == "n":
            print("The arrow was not used.\n")
            return False
        else:
            return combatitem(player)
    if "Spellbook" in player.items:
        print("Would you like to use Spellbook? [y/n]\n")
        response = input("> ").lower()
        if response == "y":
            time.sleep(1)
            damage_delt += damage_bonus
            print(f"Damage increased to {damage_delt}!\n")
            player.items.remove("Spellbook")
            print("The Spellbook crumbles into dust...")
        elif response == "stats":
            print("stats funct placeholder\n")
            return combatitem(player)
        elif response == "n":
            print("The Spellbook was not used.\n")
            return False
        else:
            return combatitem(player)
    return True, damage_delt