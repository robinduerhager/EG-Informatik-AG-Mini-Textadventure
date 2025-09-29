from enum import Enum

scenario = Enum('scenario', [('DEFAULT', 1), ('ARENA', 2), ('SHOP', 3)])


# player_action = input("""Possible Commands:
# 1 - attack
# ---
# Please input what you want to do:
# """)

# Give the player Options based on the Szenario that is currently set
# If in DEFAULT:
# Move to ARENA or SHOP or equip or unequip an Item

# If in ARENA:
# Fight or Move to -> DEFAULT

# If in SHOP:
# Buy new Item, Sell Item from Inventory or move to -> DEFAULT

def begin_game() -> None:
    while True:
        input("Press enter to continue...")
