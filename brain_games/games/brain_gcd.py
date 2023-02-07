from random import randint
from math import gcd


START_WORD = "Find the greatest common divisor of given numbers."
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def play():
    num1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{num1} {num2}'
    result = gcd(num2, num1)
    return question, result
