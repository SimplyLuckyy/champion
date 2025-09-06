import time
from actors.enemy import *
from systems.combat import battle, next_room, items_list
from text import view_stats


global potion_cost, spellbook_cost, payoff, stat_cost, attack_increase, defense_increase
potion_cost = 3
spellbook_cost = 10
payoff = 5
stat_cost = 10
attack_increase = 3
defense_increase = 3

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
    true_int = False
    cost_temp = cost
    if cost == potion_cost:
        print(f"Would you like to trade gold for potions? [{potion_cost} Gold for 1 Potion]. [y/n]\n")
    elif cost == spellbook_cost:
        print(f"Would you like to trade {spellbook_cost} gold for a Spellbook? [y/n]\n")
    choice = input("> ").lower()
    print("")
    if choice == "y":
        time.sleep(1)
        if cost == potion_cost:
            print("\nHow many potions do you want? [Integer]\n")
            choice = input("> ")
            print("")
            time.sleep(1)
            while true_int == False:
                try:
                    int(choice)
                except Exception:
                    print("Not an integer. Input an integer.\n")
                    choice = input("> ")
                    print("")

            if (int(choice) * potion_cost) > player.gold:
                print("Not enough gold.\n")
                buyitems(player, cost_temp)
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
                    buyitems(player, cost_temp)
        if cost == spellbook_cost:
            print("\nSpellbook obtained.\n")
            player.items.append(items_list[1])

    elif choice == "n":
        print("Trade declined.\n")
        return
    elif choice == "stats":
        view_stats(player)
        buyitems(player, cost_temp)
    else:
        print("Invalid Choice\n")
        buyitems(player, cost_temp)

# Magic spikes + elixirs. Lose stamina. Way to lose gold?
# Magic fountain. Throw in gold for better elixir.
def social2(player):
    time.sleep(1)
    print("This is social2")
    time.sleep(1)
    print("Spikes placeholder\n")
    print("1. Attempt to cross")
    print("2. Ignore\n")
    choice = input("> ")
    time.sleep(1)
    while choice not in ["1", "2"]:
        print("Invalid Choice.\n")
        print(f"1. Attempt to cross")
        print("2. Ignore\n")
        choice = input("> ")
        print("")
    temp = player.energy
    if choice == "1":
        if not player.arcaneknowledge:
            payoffencounter(player, player.energy, player.energyname)
        else:
            print("Arcane Knowledge Trigger placeholder\n")
        if not player.arcaneknowledge and temp < stat_cost:
            print("You left to the next room.\n")
        else:
            spikes(player)
    else:
        time.sleep(1)
        print("You ignore the spike trap.\n")
    next_room(player)

# Adventurer + explosives. Lose hp and potentially gold.
# Add option to ignore encounter
def social3(player):
    time.sleep(1)
    print("This is social3\n")
    time.sleep(1)
    print("You see a distracted and nervous adventurer in the center of the rooom.\n")
    print("1. Approach")
    print("2. Ignore\n")
    choice = input("> ")
    time.sleep(1)
    while choice not in ["1", "2"]:
        print("Invalid Choice.\n")
        print("1. Approach")
        print("2. Ignore\n")
        choice = input("> ")
    
    if choice == "1":
        temp = player.health
        if not player.keeneye:
            payoffencounter(player, player.health, "health")
        else:
            print("Keen Eye Trigger Placeholder\n")
        if temp == 1 and not player.keeneye:
            print("You escape to the next room!\n")
        else:
            adventurer(player)
    else:
        time.sleep(1)
        print("You sneak past the adventurer.\n")

    next_room(player)

def payoffencounter(player, stat, name):
    time.sleep(1)
    damage = stat_cost
    if name == "health" and player.health == 1:
        print("But you avoided the attack!\n")
    elif name == player.energyname and player.energy < stat_cost:
        print("But you didn't have enough stamina to expend!\n")
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
        time.sleep(1)
        print(f"You recieved the {items_list[3]}!")
        player.items.append(items_list[3])
    elif choice == "2":
        print("\nYou attempt to bribe.\n")
        if player.gold < payoff:
            time.sleep(1)
            print("But you didn't have enough!")
            time.sleep(1)
            print(f"You recieved the {items_list[3]}!")
            player.items.append(items_list[3])
        else:
            time.sleep(1)
            print(f"You gave {payoff} Gold.")
            time.sleep(1)
            print(f"You recieved the {items_list[4]}!\n")
            player.items.append(items_list[4])
    elif choice == "stats":
        view_stats(player)
        adventurer(player)
    else:
        print("Invalid Choice\n")
        adventurer(player)

def spikes(player):
    time.sleep(1)
    print("What will you do?\n")
    print("1. Take Elixir")
    print(f"2. Toss Gold [{payoff} Gold]\n")
    choice = input("> ")
    time.sleep(1)
    if choice == "1":
        print("\nYou scooped the elixir into a nearby bottle.\n")
        print(f"You recieved the {items_list[5]}!")
        player.items.append(items_list[5])
    elif choice == "2":
        print("\nYou reach into you gold pouch.\n")
        if player.gold < payoff:
            time.sleep(1)
            print("But you didn't have enough!")
            time.sleep(1)
            print(f"You recieved the {items_list[5]}!")
            player.items.append(items_list[5])
        else:
            time.sleep(1)
            print(f"You tossed in {payoff} Gold.")
            print("The pool shimmers and the gold disolves.")
            print(f"You recieved the {items_list[6]}!\n")
            player.items.append(items_list[6])
    elif choice == "stats":
        view_stats(player)
        spikes(player)
    else:
        print("Invalid Choice\n")
        spikes(player)

# Gold
def loot1(player):
    reward = 10
    time.sleep(1)
    print("In the room stands a lone chest.")
    time.sleep(1)
    print("The lock is worn and corroded, easily falling from the it's hook.")
    time.sleep(1)
    print(f"Inside the chest is gold! [Recieved {reward} Gold]")
    player.gold += reward
    time.sleep(1)
    print("There is nothing else of interest in the room.\n")
    next_room(player)

# Defense Boost + Magic Sheild
def loot2(player):
    time.sleep(1)
    print("In the room stands a lone chest.")
    time.sleep(1)
    print("The lock is worn and corroded, easily falling from the it's hook.")
    time.sleep(1)
    print(f"Inside the chest is armor! [Defense Increased By {defense_increase} points]")
    player.defense += defense_increase
    time.sleep(1)
    if player.arcaneknowledge:
        print("Arance Knowledge Trigger Placeholder.")
        print(f"You recieved the {items_list[2]}!")
        print(f"The {items_list[2]} allows you to negate all damage once.")
        player.items.append(items_list[2])
    print("There is nothing else of interest in the room.\n")
    next_room(player)

# Attack Boost + Barbed Arrow
def loot3(player):
    time.sleep(1)
    print("In the room stands a lone chest.")
    time.sleep(1)
    print("The lock is worn and corroded, easily falling from the it's hook.")
    time.sleep(1)
    print(f"Inside the chest is a {player.weaponname}! [Attack Increased By {attack_increase} points]")
    player.attack += attack_increase
    time.sleep(1)
    if player.keeneye:
        print("Keen Eye Trigger Placeholder.")
        time.sleep(1)
        print(f"You recieved the {items_list[0]}!")
        time.sleep(1)
        # Currently damage is increased flatly. Change to damage ignores defense?
        print(f"The {items_list[0]} allows you to [PLACEHOLDER].")
        player.items.append(items_list[0])
    time.sleep(1)
    print("There is nothing else of interest in the room.\n")
    time.sleep(1)
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
    enemy = Boss()
    time.sleep(1)
    print("This is boss\n")
    if player.arcaneknowledge:
        print("Arcane Knowledge Trigger Placeholder\n")
        playerturn(player, enemy)
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    