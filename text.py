import time
from actors.player import *


boarder = "=" * 20

# Need to write Social Floors

def warrior_description():
    time.sleep(1)
    print(boarder)
    lines = ["You are the Warrior.\n",
    "With both high Attack and Defense you are stalwart in your quest to acheive your rightful glory, regardless of who stands in your way.\n",
    "No extra interactions will be unlocked, on account of your single minded dedication."]
    for line in lines:
        time.sleep(1)
        print(line)
    time.sleep(1)
    print(boarder + "\n")

def rogue_description():
    time.sleep(1)
    print(boarder)
    lines = ["You are the Rogue.\n", "Training to avoid and redirct otherwise fatal attacks has gifted you greater Defense and Stamina, at the cost of Attack.",
    "Your honed senses give you greater awareness to your surrounds.\n",
    "Few extra interactions may be unlocked depending on the floors encountered due to your Keen Eye."]
    for line in lines:
        time.sleep(1)
        print(line)

    time.sleep(1)
    print(boarder + "\n")

def mage_description():
    time.sleep(1)
    print(boarder)
    lines = ["You are the Mage.\n", "Years studying the arcane has rewarded you with greater Attack and Mana, but your physical form remains defenseless.\n",
    "Some extra interactions will be unlocked, due to your Arcane Knowledge\n"]
    for line in lines:
        time.sleep(1)
        print(line)

    time.sleep(1)
    print(boarder + "\n")

def debug_description():
    time.sleep(1)
    print(boarder)
    lines = ["You are the Developer.\n", "This is a debug class intended for testing. It was kept in as an easter egg.", 
    "Your Attack, Defense, Health, Stamina, Gold, and starting Potions are far beyound what is necessary, making your quest trivial.\n",
    "All extra interactions will be unlocked to you."]
    for line in lines:
        time.sleep(1)
        print(line)

    time.sleep(1)
    print(boarder + "\n")

def view_stats(player):
    print(f"""{boarder}
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
    print(f"{boarder}\n")



def title():
    lines = ["   ____ _   _    _    __  __ ____ ___ ___  _   _ ",
             "  / ___| | | |  / \\  |  \\/  |  _ \\_ _/ _ \\| \\ | |",
             " | |   | |_| | / _ \\ | |\\/| | |_) | | | | |  \\| |",
             " | |___|  _  |/ ___ \\| |  | |  __/| | |_| | |\\  |",
             "  \\____|_| |_/_/   \\_\\_|  |_|_|  |___\\___/|_| \\_|",
             ""]
    time.sleep(1)
    print(boarder * 3)
    time.sleep(0.5)

    for line in lines:
        time.sleep(0.1)
        print(line)
    
    time.sleep(0.5)
    print(boarder * 3)

def introduction():
    
    title()
    lines = ["\nShrouded under ancient ruins legends tell of a grand dungeon, its architect long lost to time.",
    "Adventurers from across the nation embark on a descent into the catacombs for glory.",
    "Of the few that survive to tell their tale, the recounting of what they found is never the same.",
    "The only point the seem to agree upon is what lies at the end: A beast unlike anything seen above and riches beyond imagination.",
    "Those that manage to surpass such as beast are heralded as Champions.\n",
    "As a seasoned adventurer, that is the title you seak to claim to truly prove your mettle.",
    "But first..."]
    
    for line in lines:
        time.sleep(1)
        print(line)

def tutorial(player):
    notbegun = True
    time.sleep(1)
    print("Would you like a tutorial of the basic mechanics before you begin your quest?\n")
    print("1. Continue\n2. Help\n")
    choice = input("> ")
    print("")
    if choice == "2":
        tutorialdescription(player)
    elif choice == "1":
        notbegun = False
    else:
        print("Invalid Choice\n")
        return tutorial(player)
    time.sleep(1)
    while notbegun:
        print("Begin your quest?\n")
        print("1. Continue\n")
        choice = input("> ")
        print("")
        if choice == "1":
            notbegun = False
    time.sleep(1)
    print(boarder)

def tutorialdescription(player):
    lines = [f"{player.energyname} and Health can be replenished using potions or when encountering a Rest Room.\n",
    f"You start with {player.potions} Potions. More may be found during your quest.",
    f"Potions regain 25 points of Health and {player.energyname}.",
    "They are used automatically after attacks that would be fatal.",
    "Otherwise you must use a turn to consume a potion during battle.\n",
    "Rest Rooms are encounted every 5th room.",
    "They allow you to recover half of your currently missing health."]
    attacksmage = ["As a Mage, your energy is Mana.", 
    "Both your regular and strong attacks will cost Mana (5 and 15 respectively)",
    "If your Mana is deplated you will instead attack with your staff, dealing very minor damage."]
    attacks = [f"As a {player.name}, your energy is Stamina.",
    "Your strong attacks will cost Stamina (10), and once deplated you may only perform regular attacks."]
    time.sleep(1)
    print(boarder)
    time.sleep(1)
    print("At any time you may type 'stats' (without quotes) to view your stats.\n")

    if player.energyname == "Mana":
        for line in attacksmage:
            time.sleep(1)
            print(line)
    else:
        for line in attacks:
            time.sleep(1)
            print(line)

    for line in lines:
        time.sleep(1)
        print(line)

    print(boarder)

def first_floor_intro(player):
    notbegun = True
    lines = ["You stand before the grand doors leading into the dungeon.",
    "The hinges are rusted, creaking as you push past the bulk.",
    "Steeping past the entryway, the doors seal behind you trapping you inside.",
    "The stale air smells of rot and smoke. The only way through is down.\n",]
    
    for line in lines:
        time.sleep(1)
        print(line)
    
    while notbegun:
        time.sleep(1)
        print("Begin your descent?\n\n1. Continue\n2. Stats\n")
        choice = input("> ")
        print("")
        if choice == "1":
            notbegun = False
        elif choice == "2" or choice == "stats":
            time.sleep(1)
            view_stats(player)
    
    time.sleep(1)
    print("You descend to the first floor...")

def ending(player):
    lines = ["The beast collapses back into a heap of bones, whatever possesed it expelled by your fatal strike.",
    "It will rise again for the next aspiring champion, but until then it will lie lifeless and dormant.\n",
    "The grand chest clicks open as if it sensed your triumph.",
    "Inside lies the proof of your achievement: Mountains of gold and equipment burning with arcane energy."
    "A light shimmers from the center of the room calling to you.",
    "Before you depart you reach into the pile of bones and claim a gilded spine as your trophy.",
    "Stepping into the light it blinds you.",
    "Once your eyes open again you stand before the grand door into the dungeon.\n",
    "Returning to civilization you are welcomed with open arms as one of the few elite to accomplish such a challenge.",
    "Your exploits are proclaimed across the nation, known to all as a Champion.\n",
    boarder]

    for line in lines:
        time.sleep(1)
        print(line)
    time.sleep(1)

def socialmerchanttext():
    lines = ["A ghostly figure stands in the center of the room.",
    "When you approach an otherworldly echo emanates from their unmoving mouth.",
    '"I see yet another chooses to brave this crypt..."',
    '"I was once like you, so young and full naive courage."',
    '"Now I find my soul bound to this very room. The occasional adventurous fool my only company."',
    '"I wish to aide you on your quest, lest you end up like me."',
    'They gesture to their side, "I have a wide stock of potions you may use to replenish your strength."',
    '"All ask for in return is gold."',
    '"..."',
    '"...We all have to make a living somehow."\n']

    for line in lines:
        time.sleep(1)
        print(line)

def socialmerchantmage():
    lines = ["[Arcane Knowledge] You sense powerful necrotic magic emitted by the merchant.",
    "That must be what allowed their soul to persist past death.\n",
    'Their form flickers with recognition, "Wait."',
    '"Before you go, I have another offer to provide."',
    '"It has been so very long since I have encountered a fellow Mage."',
    '"I may have something of interest to you... While old, I promise it is worth the price."\n']

    for line in lines:
        time.sleep(1)
        print(line)

def socialadventurertext(player):
    lines = ["The young adventurer startles at the sound of your footsteps, hand flying to the hilt of their sword.",
    "They don't seem to relax even after realizing you aren't a monster, eyes jumping at the slightest movement.\n",]

    for line in lines:
        time.sleep(1)
        print(line)

def resttext(player, restore_health, restore_energy):
    lines = ["You find the next floor surprisingly empty.",
    "It appears safe, and you take the rare oppurtunity to rest.\n",
    f"You replenished {restore_health} Health and {restore_energy} {player.energyname}!\n"]

    for line in lines:
        time.sleep(1)
        print(line)