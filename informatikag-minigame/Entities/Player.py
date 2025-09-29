from Mechanics import Dice, Player_Inventory
from Entities import Item

_player_stats = {
    'name': '',
    'age': 25,
    'attributes': {
        'strength': Dice.four_sided_dice,
        'agility': Dice.six_sided_dice
    },
    'health': 100,
    'equipped_item': Item.get_default_weapon(),
}


def attack(enemy) -> None:
    # first choose a set of dice which should be used for the action
    dice_set = _choose_dice_set()
    damage_result = 0

    for dice in dice_set:
        damage_result += dice['roll']()

    enemy['take_damage'](damage_result)


def take_damage(damage):
    _player_stats['health'] = max(0, _player_stats['health'] - damage)


def _choose_dice_set():
    """
    Choose a set of dice based on the action which should be rolled for the action which is performed
    """
    dice_set = []
    damage_die = Dice.four_sided_dice
    equipped_item = _player_stats['equipped_item']

    if equipped_item['type'] in (Item.item_type.WEAPON, Item.item_type.DEFAULT):
        # If we use a Weapon, use the damage_multiplier attribute
        match equipped_item['weapon_type']:
            # First determine the damage die we should use based on the weapon attributes
            case Item.weapon_type.BLADE:
                # If we use a blade, use the strength die
                damage_die = _player_stats['attributes']['strength']
            case Item.weapon_type.FISTS:
                damage_die = _player_stats['attributes']['strength']
            case Item.weapon_type.BOW:
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

    if previously_equipped_item['type'] is not Item.get_default_weapon()['type']:
        # If the player didn't equip any item, we don't have to add 'None' into the Inventory list
        Inventory.add_item(previously_equipped_item)


def unequip():
    if _player_stats['equipped_item']['type'] is not Item.get_default_weapon()['type']:
        Inventory.add_item(_player_stats['equipped_item'])

    _player_stats['equipped_item'] = Item.get_default_weapon()
