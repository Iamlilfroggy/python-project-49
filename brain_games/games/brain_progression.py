from random import randint

START_WORD = 'What number is missing in the progression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 13

def play():
    start_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    inc_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    progression = [(start_number + i * inc_number) for i in range(10)]
    hidden_number = randint(0, 9)
    result = str(progression[hidden_number])
    progression[hidden_number] = '..'
    question = ' '.join(str(i) for i in progression)
    return question, result
