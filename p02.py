"""
    Easy problem so far, how do I set up unit testing? Plus code coverage
    would be good.
"""

from enum import Enum

class OpponentMoves(Enum):
    """ Represents opponent moves """
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

class MyMoves(Enum):
    """ Represents player moves """
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

def result(opponent_move, my_move):
    """ Returns the result of a round
        Rock - 1
        Paper - 2
        Scissors - 3

        Lose - 0
        Draw - 3
        Win - 6
    """
    if opponent_move == OpponentMoves.ROCK:
        return (3 if my_move == MyMoves.LOSE else
                4 if my_move == MyMoves.DRAW else
                8)
    if opponent_move == OpponentMoves.PAPER:
        return (1 if my_move == MyMoves.LOSE else
                5 if my_move == MyMoves.DRAW else
                9)
    if opponent_move == OpponentMoves.SCISSORS:
        return (2 if my_move == MyMoves.LOSE else
                6 if my_move == MyMoves.DRAW else
                7)
    return "error"

def run():
    """ Runs code for AoC answers """
    with open("./input.txt", 'r', encoding='UTF-8') as file:
        lines = [line.rstrip() for line in file]

    answer1 = 0
    for line in lines:
        moves = line.split()
        answer1 += result(OpponentMoves(moves[0]), MyMoves(moves[1]))

    print("Answer 1: " + str(answer1))

if __name__ == '__main__':
    run()
