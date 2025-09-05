from Mechanics import Dice
from Mechanics import Inventory

DEFAULT_WEAPON = {'type': 'DEFAULT', 'weapon_type': 'FISTS', 'name': 'Fists', 'damage_multiplier': 1}

_player_stats = {
    'name': '',
    'age': 25,
    'attributes': {
        'strength': Dice.four_sided_dice,
        'agility': Dice.six_sided_dice
    },
    'health': 100,
    'equipped_item': DEFAULT_WEAPON,
}


def attack(enemy) -> None:
    # first choose a set of dice which should be used for the action
    dice_set = _choose_dice_set()
    damage_result = 0

    for dice in dice_set:
        damage_result += dice['roll']()

    enemy['health'] -= damage_result


def _choose_dice_set():
    """
    Choose a set of dice based on the action which should be rolled for the action which is performed
    """
    dice_set = []
    damage_die = Dice.four_sided_dice
    equipped_item = _player_stats['equipped_item']

    if equipped_item['type'] in ('WEAPON', 'DEFAULT'):
        # If we use a Weapon, use the damage_multiplier attribute
        match equipped_item['weapon_type']:
            # First determine the damage die we should use based on the weapon attributes
            case 'BLADE':
                # If we use a blade, use the strength die
                damage_die = _player_stats['attributes']['strength']
            case 'FISTS':
                damage_die = _player_stats['attributes']['strength']
            case 'BOW':
                damage_die = _player_stats['attributes']['agility']
            case _:
                raise TypeError('Invalid equipped_item type')

        for x in range(equipped_item['damage_multiplier']):
            # construct the dice set based on the damage die and damage multiplier
            dice_set.append(damage_die)

    return dice_set


def equip_item(item_index) -> None:
    """
    Swap the equipped item with the inventory slot of the item which should be equipped.
    :param item_index: The Index of the item in the inventory which should be equipped.
    :return: None
    """
    previously_equipped_item = _player_stats['equipped_item']
    _player_stats['equipped_item'] = Inventory.get_item(item_index)
    Inventory.remove_item(item_index)

    if previously_equipped_item['type'] is not DEFAULT_WEAPON['type']:
        # If the player didn't equip any item, we don't have to add 'None' into the Inventory list
        Inventory.add_item(previously_equipped_item)


def unequip():
    if _player_stats['equipped_item']['type'] is not DEFAULT_WEAPON['type']:
        Inventory.add_item(_player_stats['equipped_item'])

    _player_stats['equipped_item'] = DEFAULT_WEAPON
