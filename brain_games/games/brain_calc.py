from random import randint
from random import choice


start_word = 'What is the result of the expression?'
number = randint(1, 25)


def play():
    num1 = number
    num2 = number
    decision = choice('+-*')
    question = f'{num1} {decision} {num2}'
    if decision == '+':
        result = num1 + num2
    if decision == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return result, question
