#!/usr/bin/env python3


from brain_games import greet
from brain_games.games import brain_prime


def main():
    greet.start(brain_prime)


if __name__ == '__main__':
    main()
