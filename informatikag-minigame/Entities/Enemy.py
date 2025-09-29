from Entities import Item
from Mechanics import Dice

current_enemy = {
    'health': 100,
    'weapon': Item.get_random_weapon(include_default_weapon=True),
    'base_damage_die': Dice.get_random_dice()
}

def attack(player):
    enemy_damage_value = 0

    for i in range(0, current_enemy['weapon']['damage_multiplier'] - 1):
        enemy_damage_value += current_enemy['base_damage_die'].roll()

    player['health'] -= enemy_damage_value

def take_damage(damage):
    current_enemy['health'] = max(0, current_enemy['health'] - damage)

def generate_enemy():
    global current_enemy # Else, a "new" current_enemy variable will be created, but we want to set the "global" one on the top of the file

    generated_enemy = {
        'health': 100,
        'weapon': Item.get_random_weapon(include_default_weapon=True),
        'base_damage_die': Dice.get_random_dice()
    }

    current_enemy = generated_enemy