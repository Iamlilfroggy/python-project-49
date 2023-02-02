from random import randint

start_word = 'What number is missing in the progression?'
min_length = 5  # минимальная длина прогрессии
max_length = 10  # максимальная длина прогрессии
lower_limit = 1  # минимальное стартовое число
upper_limit = 13  # максимальное стартовое число


def play():
    start_number = randint(0, 13)
    inc_number = randint(0, 13)
    progression = [(start_number + i * inc_number) for i in range(10)]
    hidden_number = randint(0, 9)
    result = str(progression[hidden_number])
    progression[hidden_number] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, result
