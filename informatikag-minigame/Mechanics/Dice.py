import random


def _roll_dice(sides: int) -> int:
    return random.randint(1, sides)


def get_random_dice():
    dice_number = random.randint(1, 6)
    match dice_number:
        case 1:
            return four_sided_dice
        case 2:
            return six_sided_dice
        case 3:
            return eight_sided_dice
        case 4:
            return ten_sided_dice
        case 5:
            return twelve_sided_dice
        case 6:
            return twenty_sided_dice

    # PyCharm wants me to add this, though there shouldn't be any case in which we run into this
    return None


four_sided_dice = {'sides': 4, 'roll': _roll_dice(4)}
six_sided_dice = {'sides': 6, 'roll': _roll_dice(6)}
eight_sided_dice = {'sides': 8, 'roll': _roll_dice(8)}
ten_sided_dice = {'sides': 10, 'roll': _roll_dice(10)}
twelve_sided_dice = {'sides': 12, 'roll': _roll_dice(12)}
twenty_sided_dice = {'sides': 20, 'roll': _roll_dice(20)}
