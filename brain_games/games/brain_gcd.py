from random import randint
from math import gcd


start_word = "Find the greatest common divisor of given numbers."


def play():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{num1} {num2}'
    result = gcd(num2, num1)
    return question, result
