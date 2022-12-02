from random import randint
from constants import CANDIES

def choose_turn():  # вибираем, кто ходит
    return randint(0, 1)

def bot_turn(candies, max_turn):  # описываем логику бота
    if 70 < candies < 100 or candies % (max_turn + 1) == 0 or candies == CANDIES:
        return randint(1, max_turn)
    else:
        if candies <= max_turn:
            return candies
        else:
            return candies % (max_turn + 1)
