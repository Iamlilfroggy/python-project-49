from random import randint


start_word = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play():
    num1 = randint(1, 100)
    question = num1
    k = 0
    for i in range(2, num1 // 2 + 1):
        if (num1 % i == 0):
            k += 1
    if (k <= 0):
        result = "yes"
    else:
        result = 'no'
    return question, result
