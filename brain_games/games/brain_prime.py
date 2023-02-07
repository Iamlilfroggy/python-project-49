from random import randint


START_WORD = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def play():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{num}'
    if is_even(num):
        result = 'yes'
    else:
        result = 'no'
    return question, result


def is_even(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count <= 2:
        return True
    else:
        return False
