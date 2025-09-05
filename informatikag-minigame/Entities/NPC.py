from Mechanics import Dice

def generate_enemy():
    return {
        'health': 100,
        'damage': Dice.get_random_dice(),
    }