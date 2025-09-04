import time
from actors.enemy import *
from systems.combat import battle, next_room, items_list
from text import view_stats

# todo list:
# Combat Rooms - DONE
# Social Rooms - 2/3
# Loot Rooms - WIP
global potion_cost, spellbook_cost, payoff, stat_cost
potion_cost = 3
spellbook_cost = 10
payoff = 5
stat_cost = 10

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
    print("This is social1\n")
    time.sleep(1)
    print("merchant placeholder\n")
    time.sleep(1)
    buyitems(player, potion_cost)
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge\n")
        time.sleep(1)
        buyitems(player, spellbook_cost)
    next_room(player)

def buyitems(player, cost):

    if cost == potion_cost:
        print(f"Would you like to trade gold for potions? [{potion_cost} Gold for 1 Potion]. [y/n]\n")
    elif cost == spellbook_cost:
        print(f"Would you like to trade {spellbook_cost} gold for a Spellbook? [y/n]\n")
    choice = input("> ").lower()
    if choice == "y":
        time.sleep(1)
        if cost == potion_cost:
            print("\nHow many potions do you want? [Integer]\n")
            choice = input("> ")
            time.sleep(1)
            try:
                int(choice)
            except Exception:
                print("Not an integer. Input an integer.")
                buypotions(player)

            if (int(choice) * potion_cost) > player.gold:
                print("Not enough gold.\n")
                buypotions(player)
            else:
                print(f"\nBuy {choice} potions for {int(choice) * potion_cost} gold? [y/n]\n")
                potion_count = int(choice)
                choice = input("> ").lower()
                if choice == "y":
                    print("\nTraded potions for gold.\n")
                    player.potions += potion_count
                    player.gold -= potion_count * potion_cost
                if choice == "n":
                    print("\nDeclined trade.\n")
                    buypotions(player)
        if cost == spellbook_cost:
            print("\nSpellbook obtained.\n")
            player.items.append(items_list[1])

    elif choice == "n":
        print("Trade declined.\n")
        return
    elif choice == "stats":
        view_stats(player)
        buypotions(player)
    else:
        print("Invalid Choice\n")
        buypotions(player)

# Magic spikes + elixirs. Lose stamina. Way to lose gold?
# Magic fountain. Throw in gold for better elixir.
def social2(player):
    time.sleep(1)
    print("This is social2")
    time.sleep(1)
    if player.arcaneknowledge:
        print("Player has Arcane Knowledge")
    next_room(player)

# Adventurer + explosives. Lose hp and potentially gold.
def social3(player):
    time.sleep(1)
    print("This is social3\n")
    time.sleep(1)
    print("Adventurer Placeholder.\n")
    time.sleep(1)
    temp = player.health
    if not player.keeneye:
        payoffencounter(player, player.health, "health")
    else:
        print("Keen Eye Trigger Placeholder\n")
    if temp == 1:
        print("You escape to the next room!\n")
    else:
        adventurer(player)
    next_room(player)

def payoffencounter(player, stat, name):
    damage = stat_cost
    if name == "health" and player.health == 1:
        print("But you avoided the attack!\n")
    elif name == player.energyname and player.energy == 0:
        print("But you had no stamina to expend!\n")
    else:
        if damage >= stat:
            damage = 0
            for i in range(stat, 0, -1):
                damage += 1
            if name == "health":
                damage -= 1
        print(f"You lose {damage} {name}!\n")
        stat -= damage
    if name == "health":
        player.health = stat
    else:
        player.energy = stat
    
def adventurer(player):
    time.sleep(1)
    print("What will you do?\n")
    print("1. Threaten")
    print(f"2. Bribe [{payoff} Gold]\n")
    choice = input("> ")
    time.sleep(1)
    if choice == "1":
        print("\nYou Threatened.\n")
        print(f"You recieved the {items_list[3]}!")
        player.items.append(items_list[3])
    elif choice == "2":
        print("\nYou attempt to bribe.\n")
        if player.gold < payoff:
            time.sleep(1)
            print("But you didn't have enough!")
            time.sleep(1)
            print("The adventurer leaves.\n")
        else:
            time.sleep(1)
            print(f"You gave {payoff} Gold.")
            print(f"You recieved the {items_list[4]}!\n")
            player.items.append(items_list[4])
    elif choice == "stats":
        view_stats(player)
        adventurer(player)
    else:
        print("Invalid Choice\n")
        adventurer(player)

def spikes(player):
    pass

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