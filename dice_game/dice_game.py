import random
import re

DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")

POSSIBLE_DICE = {"100", "20", "12", "10", "8", "6", "4", "3"}


def roll_the_dice(dice_code):
    """
    Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern ex. `7D12-5`
    :rtype: int, str
    :return: dice roll value or 'Wrong Input'
    """
    match = DICE_PATTERN.match(dice_code)
    if not match:
        return "Wrong Input"

    multiply, dice, modifier = match.groups()

    if dice not in POSSIBLE_DICE:
        return "Wrong Input"

    multiply = int(multiply) if multiply else 1
    dice = int(dice)
    modifier = int(modifier) if modifier else 0

    roll_sum = sum(random.randint(1, dice) for _ in range(multiply))
    return roll_sum + modifier


def main():
    print("Welcome to the Dice Roller!")
    while True:
        dice_code = input("Enter dice pattern (e.g., '2D10+10') or 'exit' to quit: ")
        if dice_code.lower() == 'exit':
            print("Goodbye!")
            break
        result = roll_the_dice(dice_code)
        print(f"Result: {result}")


if __name__ == '__main__':
    main()
