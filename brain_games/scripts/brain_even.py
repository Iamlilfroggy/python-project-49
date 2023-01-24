#!/usr/bin/env python3


import prompt


from random import randint


def is_number_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(1, 25)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        result = is_number_even(number)
        if result == answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print("Let's try again, " + name + '!')
            break
    if i == 3:
        print("Congratulations, " + name + '!')


if __name__ == '__main__':
    main()
