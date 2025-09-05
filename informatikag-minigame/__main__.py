from Entities import Player
from Entities import NPC


def main() -> None:
    tmp_enemy = NPC.generate_enemy()
    #player_action = input("""Possible Commands:
    #1 - attack
    #---
    #Please input what you want to do:
    #""")
    while tmp_enemy['health'] > 0:
        Player.attack(tmp_enemy)
        print('Remaining health of enemy: ' + str(tmp_enemy['health']))


if __name__ == "__main__":
    main()
