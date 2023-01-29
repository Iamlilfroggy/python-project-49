from random import randint
from random import choice


start_word = 'What is the result of the expression?'


def play():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    operator = choice('+-*')
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        result = num1 + num2
    if operator == '-':
        result = num1 - num2
    if operator == '*':
        result = num1 * num2
    return question, result
