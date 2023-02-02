#!/usr/bin/env python3


from brain_games import greet
from brain_games.games import brain_progression


def main():
    greet.start(brain_progression)


if __name__ == '__main__':
    main()
