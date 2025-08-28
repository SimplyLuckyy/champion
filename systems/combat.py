from text import boarder, view_stats
from actors.player import Player
from actors.enemy import Enemy
import random
import time

global restore
restore = 25

def battle(player, enemy):
    while True:
        dodamage(enemy, player, "regular")
        print(f"player health: {player.health}\n")
        if player.health <= 0:
            break
        playerturn(player, enemy)
        print(f"enemy health: {enemy.health}\n")
        if enemy.health <= 0:
            break
    healthcheck(player, enemy)


def healthcheck(player, enemy):
    if player.health <= 0 and player.health > -(restore):
        if player.potions > 0:
            usepotion(player)
            playerturn(player, enemy)
            battle(player, enemy)
        else:
            print("Your champion has fallen\n")
            print(boarder + "\nGAME OVER\n" + Boarder)
            exit()


def playerturn(player, enemy):
    print("What will you do?\n")
    print("- Regular Attack")
    print("- Strong Attack")
    if player.potions > 0:
        print("- Use Potion")
    print("")

    choice = input("> ").lower()
    if choice == "regular" or choice == "regular attack":
        dodamage(player, enemy, "regular")
    elif choice == "strong" or choice == "strong attack":
        dodamage(player, enemy, "strong")
    elif (choice == "potion" or choice == "use potion") and player.potions > 0:
        usepotion(player)
    elif choice == "stats":
        view_stats(player)
        return playerturn(player, enemy)
    else:
        print("Invaild Choice\n")
        return playerturn(player, enemy)

def dodamage(attacker, defender, attack_type="regular"):
    if attack_type == "strong":
        damage_delt = (attacker.attack * 3) - defender.defense
        if isinstance(attacker, Player) and attacker.energyname == "Mana":
            attacker.energy -= 5
        attacker.energy -= 10
    elif attack_type == "regular":
        damage_delt = (attacker.attack * 2) - defender.defense
        if isinstance(attacker, Player) and attacker.energyname == "Mana":
            attacker.energy -= 5
    time.sleep(1)
    print(f"{attacker.name} deals {damage_delt} damage")
    if damage_delt <= 0:
        return
    if isinstance(defender, Player) and "Magic Sheild" in defender.items: 
        if not magicsheild(defender): 
            defender.health -= damage_delt
            return
    if isinstance(attacker, Player) and ("Barbed Arrow" in attacker.items or "Spellbook" in attacker.items):
        (using, damage_delt) = combatitem(attacker, damage_delt)
        if using:
            defender.health -= damage_delt
            return
    
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
        view_stats()
        return magicsheild(player)
    elif response == "n":
        print("Damge not negated\n")
        return False
    else:
        print("Invaild Choice\n")
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
            view_stats(player)
            return combatitem(player, damage_delt)
        elif response == "n":
            print("The arrow was not used.\n")
            return False, damage_delt
        else:
            print("Invaild Choice\n")
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
            view_stats(player)
            return combatitem(player, damage_delt)
        elif response == "n":
            print("The Spellbook was not used.\n")
            return False, damage_delt
        else:
            return combatitem(player)
    return True, damage_delt

def usepotion(player):
    print(f"Used Potion! 25 Health and 25 {player.energyname} restored.\n")
    player.potions -= 1
    player.health += restore
    player.energy += restore


def next_room(player):
    print("Continue your descent?\n")
    print("- Continue")
    print("- Stats")
    if player.potions > 0:
        print("- Use Potion")
    print("")

    choice = input("> ").lower()
    if choice == "continue":
        pass
    elif (choice == "potion" or choice == "use potion") and player.potions > 0:
        usepotion(player)
        next_room(player)
    elif choice == "stats":
        view_stats(player)
        next_room(player)
    else:
        print("Invalid Choice")
        next_room(player)

