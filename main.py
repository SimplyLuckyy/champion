from text.intro import *

def main ():

    print(boarder + "\nPLACEHOLDER FOR INTRO\n" + boarder)
    time.sleep(1)
    player = choose_champion()

    #transform into the Check Stats function

    print(f"""{boarder}STATS

Class: {player.champion}
Health: {player.health}
{player.energyname}: {player.energy}
Gold: {player.gold}
Attack: {player.attack}
Defense: {player.defense}
Extra Ability: {player.ability}
{boarder}""")

if __name__ == "__main__":
    main()