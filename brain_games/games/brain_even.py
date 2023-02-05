from random import randint


start_word = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    num = randint(1, 100)
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
