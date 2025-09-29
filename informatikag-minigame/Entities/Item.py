import random
from enum import Enum

item_type = Enum('item_type', [('DEFAULT', 1), ('WEAPON', 2)])
weapon_type = Enum('weapon_type', [('FISTS', 1), ('BLADE', 2), ('BOW', 3)])

_items = {
    'WEAPONS': [
        # Default weapon is always on index 0
        {'type': item_type.DEFAULT, 'weapon_type': weapon_type.FISTS, 'name': 'Fists', 'damage_multiplier': 1},
        {'type': item_type.WEAPON, 'weapon_type': weapon_type.BLADE, 'name': 'blade_test', 'damage_multiplier': 2},
        {'type': item_type.WEAPON, 'weapon_type': weapon_type.BOW, 'name': 'bow_test', 'damage_multiplier': 3}
    ],
    #'ARMOUR': [], #TODO: Implement more Item Types
    #'CONSUMABLES': [],
}


def get_default_weapon():
    return _items['WEAPONS'][0]


def get_random_weapon(include_default_weapon=False):
    return _items['WEAPONS'][random.randint(0 if include_default_weapon else 1, len(_items['WEAPONS']) - 1)]
