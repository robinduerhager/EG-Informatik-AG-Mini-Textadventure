import random
from enum import Enum

item_type = Enum('item_type', [('WEAPONS', 1)])
weapon_type = Enum('weapon_type', [('DEFAULT', 1), ('BLADE', 2), ('BOW', 3)])

_items = {
    'WEAPONS': [
        # Default weapon is always on index 0
        {'type': item_type.WEAPONS, 'weapon_type': weapon_type.DEFAULT, 'name': 'Fists', 'damage_multiplier': 1, 'price': 10},
        {'type': item_type.WEAPONS, 'weapon_type': weapon_type.BLADE, 'name': 'blade_test', 'damage_multiplier': 2, 'price': 20},
        {'type': item_type.WEAPONS, 'weapon_type': weapon_type.BOW, 'name': 'bow_test', 'damage_multiplier': 3, 'price': 30}
    ],
    #'ARMOUR': [], #TODO: Implement more Item Types
    #'CONSUMABLES': [],
}

def list_items() -> None:
    print("""Shop Items:
ID - NAME - PRICE""")
    for idx, item in enumerate(_items['WEAPONS']):
        if idx == 0:
            continue
        print(str(idx) + ' - ' + item['name'] + ' - ' + str(item['price']))

    print() # Prints a new line so it looks a bit better in the output

def get_default_weapon():
    return _items['WEAPONS'][0]


def get_random_weapon(include_default_weapon=False):
    return _items['WEAPONS'][random.randint(0 if include_default_weapon else 1, len(_items['WEAPONS']) - 1)]

def get_item(item_index):
    return _items['WEAPONS'][item_index]