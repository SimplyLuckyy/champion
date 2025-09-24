import time
from actors.enemy import *
from systems.combat import battle, next_room, items_list, playerturn
from text import view_stats, resttext, socialmerchanttext, socialadventurertext, socialmerchantmage


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
        print(f"[Keen Eye] You are alerted to its weak points.\n{enemy.name}'s defenses reduced!\n")
        enemy.defense -= 5
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} Defeated!\n")
    next_room(player)

# Potion Merchant + Spellbook
def social1(player):

    time.sleep(1)
    socialmerchanttext()
    time.sleep(1)
    buyitems(player, potion_cost)
    time.sleep(1)
    if player.arcaneknowledge:
        socialmerchantmage()
        time.sleep(1)
        buyitems(player, spellbook_cost)
    time.sleep(1)
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
            print("How many potions do you want? [Integer]\n")
            choice = input("> ")
            print("")
            time.sleep(1)
            while true_int == False:
                try:
                    if int(choice) == 0:
                        print("Input an integer greater than 0.\n")
                        true_int = False
                        choice = input("> ")
                        print("")
                    else:
                        true_int = True
                except Exception:
                    print("Not an integer. Input an integer.\n")
                    choice = input("> ")
                    print("")

            if (int(choice) * potion_cost) > player.gold:
                time.sleep(1)
                print("Not enough gold.\n")
                time.sleep(1)
                buyitems(player, cost_temp)
            elif int(choice) == 0:
                time.sleep(1)

            else:
                print(f"Buy {choice} potions for {int(choice) * potion_cost} gold? [y/n]\n")
                potion_count = int(choice)
                choice = input("> ").lower()
                print("")
                if choice == "y":
                    time.sleep(1)
                    print('"...Thank you for your donation"\n')
                    player.potions += potion_count
                    player.gold -= potion_count * potion_cost
                elif choice == "n":
                    time.sleep(1)
                    print("Declined trade.\n")
                    time.sleep(1)
                    buyitems(player, cost_temp)
                else:
                    time.sleep(1)
                    print("Invalid Choice\n")
                    time.sleep(1)
                    buyitems(player, cost_temp)
        if cost == spellbook_cost:
            time.sleep(1)
            print(f"You recieved the {items_list[1]}!")
            time.sleep(1)
            print(f"The {items_list[1]} allows you to ignore all defenses once.\n")
            player.items.append(items_list[1])
            player.gold -= spellbook_cost

    elif choice == "n":
        time.sleep(1)
        print("Trade declined.\n")
        return
    elif choice == "stats":
        time.sleep(1)
        view_stats(player)
        time.sleep(1)
        buyitems(player, cost_temp)
    else:
        time.sleep(1)
        print("Invalid Choice\n")
        time.sleep(1)
        buyitems(player, cost_temp)

# Magic spikes + elixirs. Lose stamina. Way to lose gold?
# Magic fountain. Throw in gold for better elixir.
def social2(player, started=False):
    if started == False:
        time.sleep(1)
        print("In the room resides a pit of spikes.")
        time.sleep(1)
        print("On the opposite wall sits a shimmering fountain.")
        time.sleep(1)
        print("There are platforms above the spikes providing a path.")
        time.sleep(1)
        print("However, they seem to be moving in unpredictable patterns along invisible rails.\n")
    if player.arcaneknowledge:
        time.sleep(1)
        print("[Arcane Knowledge] You sense the magic pulling at the platforms, allowing you to predict their movements.\n")
    time.sleep(1)
    choice = spikeschoice(player)
    temp = player.energy
    if choice == "1":
        if not player.arcaneknowledge:
            time.sleep(1)
            print("You attempt to cross the pit...")
            time.sleep(1)
            if player.energy >= stat_cost:
                print("And you succeeded!\n")
            payoffencounter(player, player.energy, player.energyname)
        else:
            time.sleep(1)
            print("You carefully follow the pattern of the platforms to make your way across.\n")
        if not player.arcaneknowledge and temp < stat_cost:
            print("You left to the next room.")
        else:
            time.sleep(1)
            print("Now on the other side you have a clearer look at the shimmering fountain.")
            time.sleep(1)
            print("From it springs a fortifying elixir.")
            time.sleep(1)
            print("Words glimmer above the fountain etched into the stone wall.\n")
            time.sleep(1)
            print('"Pay your respects to us with gold, O Adventurer, and see your boon strengthened"\n')
            spikes(player)
    elif choice == "2":
        time.sleep(1)
        print("You ignore the spike pit.")
    else:
        time.sleep(1)
        view_stats(player)
        social2(player, True)

    if started == True:
        return
    time.sleep(1)
    print("")
    next_room(player)

# Adventurer + explosives. Lose hp and potentially gold.
# Add option to ignore encounter
def social3(player, started=False):
    if started == False:
        time.sleep(1)
        print("You see a distracted and nervous adventurer in the center of the rooom.\n")
    time.sleep(1)
    print("What will you do?\n")
    print("1. Approach")
    print("2. Ignore\n")
    choice = input("> ")
    print("")
    time.sleep(1)
    while choice not in ["1", "2", "stats"]:
        print("Invalid Choice.\n")
        print("1. Approach")
        print("2. Ignore\n")
        choice = input("> ")
        print("")
    
    if choice == "1":
        temp = player.health
        time.sleep(1)
        print("You approach the nervous adventurer.\n")
        socialadventurertext()
        time.sleep(1)
        if not player.keeneye:
            print("Without warning they draw their sword and strike you!\n")
            time.sleep(1)
            payoffencounter(player, player.health, "health")
        else:
            print("[Keen Eye] You notice them grip on their sword's hilt tighter, preparing to stike.")
            time.sleep(1)
            print("You easily dodge the attack!\n")
        if temp == 1 and not player.keeneye:
            print("You escape to the next room!\n")
        else:
            adventurer(player)
    elif choice == "2":
        time.sleep(1)
        print("You sneak past the adventurer.")
    else:
        time.sleep(1)
        view_stats(player)
        social3(player, True)

    if started == True:
        return
    time.sleep(1)
    print("")
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
    print("")
    time.sleep(1)
    if choice == "1":
        print(f"You draw your {player.weaponname} in warning.\n")
        time.sleep(1)
        print('"I-I\'m sorry!"')
        time.sleep(1)
        print('"I hardly know what I\'m doing here."')
        time.sleep(1)
        print('"I heard there was gold to be made, but I don\'t think I\'m cut out for this."')
        time.sleep(1)
        print('"Take this as my apology. Not Like I need it anymore..."\n')
        time.sleep(1)
        print(f"You recieved the {items_list[3]}!")
        time.sleep(1)
        print(f"The {items_list[3]} allows you to do flat damage, ignoring defense.")
        player.items.append(items_list[3])
    elif choice == "2":
        print("You attempt to bribe.\n")
        if player.gold < payoff:
            time.sleep(1)
            print("But you didn't have enough!\n")
            time.sleep(1)
            print('"You\'re giving me gold? After I attacked you?"')
            time.sleep(1)
            print('"It\'s not much... but I appreicate the gesture."')
            time.sleep(1)
            print('"I heard there was gold to be made here, but I don\'t think I\'m cut out for this."')
            time.sleep(1)
            print('"Take this as my apology. Not Like I need it anymore..."\n')
            time.sleep(1)
            print(f"You recieved the {items_list[3]}!")
            time.sleep(1)
            print(f"The {items_list[3]} allows you to do flat damage, ignoring defense.")
            player.items.append(items_list[3])
        else:
            time.sleep(1)
            print(f"You offered {payoff} Gold.")
            time.sleep(1)
            print('"You\'re giving me gold? After I attacked you?"')
            time.sleep(1)
            print('"I don\'t deserve this kindness... but thank you."')
            time.sleep(1)
            print('"I came here because I heard there was gold to be made, but if you\'re giving it away I have no reason to stay"')
            time.sleep(1)
            print('"Here take this as my apology. Not like I need it anymore."\n')
            time.sleep(1)
            print(f"You recieved the {items_list[4]}!")
            time.sleep(1)
            print(f"The {items_list[4]} allows you to do flat damage, ignoring defense.")
            player.items.append(items_list[4])
            player.gold -= payoff
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
    print("")
    time.sleep(1)
    if choice == "1":
        print("You scooped the elixir into an empty bottle.\n")
        time.sleep(1)
        print(f"You recieved the {items_list[5]}!")
        time.sleep(1)
        print(f"The {items_list[5]} allows you to lessen damage in response to an attack.")
        player.items.append(items_list[5])
    elif choice == "2":
        print("You reach into you gold pouch.\n")
        if player.gold < payoff:
            time.sleep(1)
            print("But you didn't have enough!")
            time.sleep(1)
            print(f"You recieved the {items_list[5]}!")
            time.sleep(1)
            print(f"The {items_list[5]} allows you to lessen damage in response to an attack.")
            player.items.append(items_list[5])
        else:
            time.sleep(1)
            print(f"You tossed in {payoff} Gold.")
            time.sleep(1)
            print("The pool shimmers and the gold disolves.")
            time.sleep(1)
            print(f"You recieved the {items_list[6]}!")
            time.sleep(1)
            print(f"The {items_list[6]} allows you to lessen damage in response to an attack.")
            player.items.append(items_list[6])
            player.gold -= payoff
    elif choice == "stats":
        view_stats(player)
        spikes(player)
    else:
        print("Invalid Choice\n")
        spikes(player)

def spikeschoice(player):
    print("What will you do?\n")
    if player.arcaneknowledge:
        print("1. Attempt to cross")
    else:
        print(f"1. Attempt to cross [{stat_cost} Stamina]")
    print("2. Ignore\n")
    choice = input("> ")
    print("")
    time.sleep(1)
    if choice == "1":
        return "1"
    elif choice == "2":
        return "2"
    elif choice == "stats":
        view_stats(player)
        return spikeschoice(player)
    else:
        return spikeschoice(player)

# Gold
def loot1(player):
    reward = 10
    time.sleep(1)
    print("In the room stands a lone chest.")
    time.sleep(1)
    print("The lock is worn and corroded, easily falling from the its hook.")
    time.sleep(1)
    print(f"Inside the chest is gold! [Recieved {reward} Gold]")
    player.gold += reward
    time.sleep(1)
    print("There is nothing else of interest in the room.\n")
    time.sleep(1)
    next_room(player)

# Defense Boost + Magic Sheild
def loot2(player):
    time.sleep(1)
    print("In the room stands a lone chest.")
    time.sleep(1)
    print("The lock is worn and corroded, easily falling from the its hook.")
    time.sleep(1)
    print(f"Inside the chest is armor! [Defense Increased By {defense_increase} points]")
    player.defense += defense_increase
    time.sleep(1)
    if player.arcaneknowledge and items_list[2] not in player.items:
        print("[Arance Knowledge] You sense arcane energy surrounding an inconspicuous ring.")
        time.sleep(1)
        print("Your magic attunes to the ring.")
        time.sleep(1)
        print(f"\nYou recieved the {items_list[2]}!")
        time.sleep(1)
        print(f"The {items_list[2]} allows you to negate all damage once.\n")
        player.items.append(items_list[2])
        time.sleep(1)
    print("There is nothing else of interest in the room.\n")
    time.sleep(1)
    next_room(player)

# Attack Boost + Barbed Arrow
def loot3(player):
    time.sleep(1)
    print("In the room stands a lone chest.")
    time.sleep(1)
    print("The lock is worn and corroded, easily falling from the its hook.")
    time.sleep(1)
    print(f"Inside the chest is a {player.weaponname}! [Attack Increased By {attack_increase} points]")
    player.attack += attack_increase
    time.sleep(1)
    if player.keeneye and items_list[0] not in player.items:
        print("[Keen Eye] You notice a barbed arrow head buried under cobwebs.")
        time.sleep(1)
        print("You fasten the head to one of your arrows.")
        time.sleep(1)
        print(f"\nYou recieved the {items_list[0]}!\n")
        time.sleep(1)
        # Currently damage is increased flatly. Change to damage ignores defense? (Later edit: Changed)
        print(f"The {items_list[0]} allows you to ignore all defenses once.")
        player.items.append(items_list[0])
    time.sleep(1)
    print("There is nothing else of interest in the room.\n")
    time.sleep(1)
    next_room(player)

# Restore 50% of lost health & energy
def rest_room(player):

    restore_health = 0
    restore_energy = 0

    if player.health < player.healthmax:
        restore_health = ((player.healthmax - player.health) // 2) + 1
        player.health += restore_health
    
    if player.energy < player.energymax:
        restore_energy = ((player.energymax - player.energy) // 2) + 1
        player.energy += restore_energy

    resttext(player, restore_health, restore_energy)
    next_room(player)


# Auuuuuuughhhhhhh
def boss_room(player):
    enemy = Boss()
    time.sleep(1)
    print("The room seems strangely empty aside from a pile of bones and a gilded chest at the back wall.\n")
    if player.arcaneknowledge:
        time.sleep(1)
        print("[Arcane Knowledge] The bones call to you. From them you sense an ancient curse.")
        time.sleep(1)
        print("This beast has risen many times to face against adventurers like you.")
        time.sleep(1)
        print("Now is your chance before it awakens to attempt to dispel the curse binding it to this crypt.")
        time.sleep(1)
        print(f"As you raise your {player.weaponname} the beast stirs, bones rising and piecing themselves together and eyes burning to life.")
        time.sleep(1)
        print("The beast stumbles as you finish your incantation. You feel its mortal presence weaken!\n")
        time.sleep(1)
        enemy.health -= 20
        player.energy -= 10
    else:
        time.sleep(1)
        print("You approach the chest. The lock is sturdy and will take great effort to break.")
        time.sleep(1)
        print("From behind you hearing sounds of creaking and burning.")
        time.sleep(1)
        print("Just in time you turn to see a great beast forming itself from the scattered bones. Its eyes burn with animalistic fury.\n")
    time.sleep(1)
    print("The beast roars, bearing rows upon rows of rotting teeth.")
    time.sleep(1)
    print("Its spines graze against the ceiling as it streches to full height.")
    time.sleep(1)
    print("With hardly any time to defend yourself the beast launches foward to strike!\n")
    time.sleep(1)
    battle(player, enemy)
    if enemy.health <= 0:
        print(f"{enemy.name} was Defeated!\n")
    