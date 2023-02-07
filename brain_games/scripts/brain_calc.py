#!/usr/bin/env python3


from brain_games import game_engine
from brain_games.games import brain_calc


def main():
    game_engine.start(brain_calc)


if __name__ == '__main__':
    main()
