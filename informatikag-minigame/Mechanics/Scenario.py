from enum import Enum

scenario = Enum('scenario', [('DEFAULT', 1), ('ARENA', 2), ('SHOP', 3)])

# If in DEFAULT:
# Move to ARENA or SHOP or equip or unequip an Item

# If in ARENA:
# Fight or Move to -> DEFAULT

# If in SHOP:
# Buy new Item, Sell Item from Inventory or move to -> DEFAULT