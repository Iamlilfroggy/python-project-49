from random import randint


start_word = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(number):
    result = 'yes'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            result = 'no'
        i += 1
    return result


def play():
    number = randint(3, 100)
    result = prime_check(number)
    question = f'Question: {number}'
    return question, result
