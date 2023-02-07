from random import randint


START_WORD = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def play():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{num}'
    if is_even(num) is True:
        result = 'yes'
    else:
        result = 'no'
    return question, result


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
