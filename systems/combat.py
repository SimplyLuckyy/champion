from text import boarder, view_stats
from actors.player import Player
from actors.enemy import Enemy
import random
import time



global restore
restore = 25

global items_list
items_list = ["Barbed Arrow", "Spellbook", "Magic Shield", "Minor Explosive", "Major Explosive", "Elixir of Fortification", "Potent Elixir of Fortification"]

global flatdamageregular, flatdamagestrong
flatdamageregular = 20
flatdamagestrong = 30

global flatreductionregular, flatreductionstrong
flatreductionregular = 10
flatreductionstrong = 20

def battle(player, enemy):
    if enemy.health <= 0:
        return
    while True:
        dodamage(enemy, player, "regular")
        time.sleep(1)
        print(f"Player Health: {player.health}")
        print(f"{enemy.name} Health: {enemy.health}\n")
        if player.health <= 0:
            break
        time.sleep(1)
        playerturn(player, enemy)
        time.sleep(1)
        print(f"Player Health: {player.health}")
        print(f"{enemy.name} Health: {enemy.health}\n")
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
            print("Your Champion has fallen.\n")
            print(boarder + "\nGAME OVER\n" + boarder)
            exit()


def playerturn(player, enemy):
    print("What will you do?\n")
    print("1. Regular Attack")
    print("2. Strong Attack")

    can_use_potion = False
    # bomb normal
    can_use_item1_1 = False
    # bomb Potent
    can_use_item1_2 = False
    energy_cost = 10
    ismage = False

    if player.energyname == "Mana":
        energy_cost = 5
        ismage = True

    if player.potions > 0:
        print("3. Use Potion")
        can_use_potion = True
    if player.potions > 0 and (items_list[3] in player.items or items_list[4] in player.items):
        if items_list[3] in player.items:
            print(f"4. Use {items_list[3]}")
            can_use_potion = True
            can_use_item1_1 = True

        if items_list[4] in player.items:
            print(f"4. Use {items_list[4]}")
            can_use_potion = True
            can_use_item1_2 = True

    if player.potions == 0 and (items_list[3] in player.items or items_list[4] in player.items):
        can_use_potion = False
        if items_list[3] in player.items:
            print(f"3. Use {items_list[3]}")
            can_use_item1_1 = True
        if items_list[4] in player.items:
            print(f"3. Use {items_list[4]}")
            can_use_item1_2 = True

    print("")

    choice = input("> ").lower()
    print("")
    if ismage == False and choice == "1":
        dodamage(player, enemy, "regular")
    elif ismage == False and choice == "2" and player.energy >= energy_cost:
        dodamage(player, enemy, "strong")
    elif ismage == False and choice == "2" and player.energy < energy_cost:
        time.sleep(1)
        print("But you didn't have enough energy!")
        dodamage(player, enemy, "regular")

    # Mage Attacks

    elif ismage and choice == "1" and player.energy >= energy_cost:
        dodamage(player, enemy, "regular")
    elif ismage and choice == "2" and player.energy >= (energy_cost + 10):
        dodamage(player, enemy, "strong")
    elif ismage and choice == "2" and player.energy < (energy_cost + 10):
        time.sleep(1)
        print("But you didn't have enough energy!")
        if player.energy >= energy_cost:
            dodamage(player, enemy, "regular")
        else:
             dodamage(player, enemy, "weak")
    elif ismage and choice == "1" and player.energy < energy_cost:
        time.sleep(1)
        print("But you didn't have enough energy!")
        dodamage(player, enemy, "weak")

    # Optional Additions
    elif choice == "3" and can_use_potion:
        usepotion(player)
    elif choice == "3" and can_use_item1_1:
        dodamage(player, enemy, flatdamageregular)
        player.items.remove(items_list[3])

    elif choice == "3" and can_use_item1_2:
        dodamage(player, enemy, flatdamagestrong)
        player.items.remove(items_list[4])

    elif choice == "4" and can_use_item1_1 and player.potions != 0:
        dodamage(player, enemy, flatdamageregular)
        player.items.remove(items_list[3])

    elif choice == "4" and can_use_item1_2 and player.potions != 0:
        dodamage(player, enemy, flatdamagestrong)
        player.items.remove(items_list[4])

    elif choice == "stats":
        view_stats(player)
        return playerturn(player, enemy)
    else:
        print("Invalid Choice\n")
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
    elif attack_type == "weak":
        damage_delt = 10 + attacker.attack - 15
    elif attack_type == flatdamageregular:
        damage_delt = flatdamageregular
    elif attack_type == flatdamagestrong:
        damage_delt = flatdamagestrong
    time.sleep(1)
    print(f"{attacker.name} deals {damage_delt} damage\n")
    if damage_delt <= 0:
        return

    # Elixir
    if isinstance(defender, Player):
        if items_list[5] in defender.items or items_list[6] in defender.items:
            damage_delt = useelixir(defender, damage_delt)
    # Magic Shield
        if items_list[2] in defender.items: 
            if not magicshield(defender): 
                defender.health -= damage_delt
            return
    # Barbed Arrow & Spellbook    
    if isinstance(attacker, Player) and (items_list[0] in attacker.items or items_list[1] in attacker.items) and (attack_type == "regular" or attack_type == "strong"):
        (using, damage_delt) = combatitem(attacker, damage_delt, attack_type)
        if using:
            defender.health -= damage_delt
            return
    
    defender.health -= damage_delt
        
def magicshield(player):
    print("Would you like to negate damage? [y/n]\n")
    choice = input("> ").lower()
    print("")
    if choice == "y":
        time.sleep(1)
        print("Damage Negated!\n")
        player.items.remove("Magic Shield")
        print("The Magic Shield shatters...\n")
        return True
    elif choice == "stats":
        view_stats()
        return magicshield(player)
    elif choice == "n":
        print("Damge not negated\n")
        return False
    else:
        print("Invalid Choice\n")
        return magicshield(player)

# Change to negating defense
def combatitem(player, damage_delt, attack_type):
    if attack_type == "strong":
        multiplier = 3
    else:
        multiplier = 2

    if "Barbed Arrow" in player.items:
        print("Would you like to use the Barbed Arrow? [y/n]\n")
        choice = input("> ").lower()
        print("")
        if choice == "y":
            time.sleep(1)
            damage_delt = player.attack * multiplier
            print(f"Damage increased to {damage_delt}!\n")
            player.items.remove("Barbed Arrow")
            print("The arrow was used up...")
        elif choice == "stats":
            view_stats(player)
            return combatitem(player, damage_delt, attack_type)
        elif choice == "n":
            print("The arrow was not used.\n")
            return False, damage_delt
        else:
            print("Invalid Choice\n")
            return combatitem(player, damage_delt, attack_type)
    if "Spellbook" in player.items:
        print("Would you like to use Spellbook? [y/n]\n")
        choice = input("> ").lower()
        print("")
        if choice == "y":
            time.sleep(1)
            damage_delt = player.attack * multiplier
            print(f"Damage increased to {damage_delt}!\n")
            player.items.remove("Spellbook")
            print("The Spellbook crumbles into dust...")
        elif choice == "stats":
            view_stats(player)
            return combatitem(player, damage_delt, attack_type)
        elif choice == "n":
            print("The Spellbook was not used.\n")
            return False, damage_delt
        else:
            return combatitem(player, damage_delt, attack_type)
    return True, damage_delt

def useelixir(player, damage_delt):
    if items_list[5] in player.items:
        print(f"Would you like to reduce damage by {flatreductionregular}? [y/n]\n")
        choice = input("> ").lower()
        print("")
        if choice == "y":
            time.sleep(1)
            print(f"Damage Reduced by {flatreductionregular}!\n")
            player.items.remove("Elixir of Fortification")
            damage_delt -= flatreductionregular
            return damage_delt
        elif choice == "stats":
            view_stats()
            return useelixir(player, damage_delt)
        elif choice == "n":
            print("Damge not reduced\n")
            return damage_delt
        else:
            print("Invalid Choice\n")
            return useelixir(player, damage_delt)
            
    elif items_list[6] in player.items:
        print(f"Would you like to reduce damage by {flatreductionstrong}? [y/n]\n")
        choice = input("> ").lower()
        if choice == "y":
            time.sleep(1)
            print(f"Damage Reduced by {flatreductionstrong}!\n")
            player.items.remove("Potent Elixir of Fortification")
            damage_delt -= flatreductionstrong
            return damage_delt
        elif choice == "stats":
            view_stats()
            return useelixir(player, damage_delt)
        elif choice == "n":
            print("Damge not reduced\n")
            return damage_delt
        else:
            print("Invalid Choice\n")
            return useelixir(player, damage_delt)

def usepotion(player):
    time.sleep(1)
    print(f"Used Potion! 25 Health and 25 {player.energyname} restored.\n")
    player.potions -= 1
    player.health += restore
    player.energy += restore
    if player.health > player.healthmax:
        player.health = player.healthmax
    if player.energy > player.energymax:
        player.energy = player.energymax
    time.sleep(1)


def next_room(player):
    print("Continue your descent?\n")
    print("1. Continue")
    print("2. Stats")
    if player.potions > 0:
        print("3. Use Potion")
    print("")

    choice = input("> ").lower()
    print("")
    if choice == "1":
        pass
    elif choice == "3" and player.potions > 0:
        usepotion(player)
        next_room(player)
    elif choice == "stats" or choice == "2":
        view_stats(player)
        next_room(player)
    else:
        print("Invalid Choice\n")
        next_room(player)

# Brainstorm:
# If Explosives are flat damage might want to buff barbed arrow & spellbook.
# Maybe Barbed Arrow & Spellbook do lingering damage? (Barbs cause injury, Spell is burning?)
# Or maybe they change the multiplier instead? 
# They will negate defense instead, to match magic shield