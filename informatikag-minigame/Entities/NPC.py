from Entities import Item
from Mechanics import Dice

def generate_enemy():
    generated_enemy = {
        'health': 100,
        'weapon': Item.get_random_weapon(include_default_weapon=True),
        'base_damage_die': Dice.get_random_dice()
    }

    def _attack(player):
        enemy_damage_value = 0

        for i in range(0, generated_enemy['weapon']['damage_multiplier']-1):
             enemy_damage_value += generated_enemy['base_damage_die'].roll()

        player['health'] -= enemy_damage_value

    def _take_damage(damage):
        generated_enemy['health'] = max(0, generated_enemy['health'] - damage)

    generated_enemy['attack'] = _attack
    generated_enemy['take_damage'] = _take_damage

    return generated_enemy