#!/usr/bin/env python3


from brain_games import greet
from brain_games.games import brain_even


def main():
    greet.start(brain_even)


if __name__ == '__main__':
    main()
