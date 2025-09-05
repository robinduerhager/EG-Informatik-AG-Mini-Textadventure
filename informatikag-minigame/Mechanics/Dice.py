import random
from functools import partial
from typing import Any


def _roll_dice(sides: int) -> int:
    return random.randint(1, sides)


def _make_dice(sides: int) -> dict[str, Any]:
    # To add a function to a dictionary we can use 'partial' or 'lambda'.
    # Though, since we create the dict and simultaneously add the roll function to it by referencing the 'sides' value, we have to use lambda,
    # because lambda will always reevaluate generated_dice['sides'] and partial won't.
    generated_dice = {'sides': sides, 'roll': lambda: _roll_dice(generated_dice['sides'])}
    return generated_dice


def get_random_dice():
    dice_number = random.randint(1, 5)
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

    # PyCharm wants me to add this, though there shouldn't be any case in which we run into this
    return None


four_sided_dice = _make_dice(4)
six_sided_dice = _make_dice(6)
eight_sided_dice = _make_dice(8)
ten_sided_dice = _make_dice(10)
twelve_sided_dice = _make_dice(12)
