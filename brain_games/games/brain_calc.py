from random import randint
from random import choice


START_WORD = 'What is the result of the expression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 25


def play():
    num1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    num2 = randint(LOWER_LIMIT, UPPER_LIMIT)
    operator = choice('+-*')
    question = f'{num1} {operator} {num2}'
    result = str(get_result(num1, operator, num2))
    return question, result


def get_result(num1, operator, num2):
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return correct_answer
