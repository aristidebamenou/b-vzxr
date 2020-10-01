#! /usr/bin/env python3
# coding: utf-8

import os
from board import Board


def main():
    position = ()

    """ Opening the universe.txt file and retrieving the size of the board """
    universe = open('./universe.txt', 'r')
    width = int(universe.readline().split(':')[1].strip())
    height = int(universe.readline().split(':')[1].strip())
    universe.close()

    """Creation of the chessboard"""
    board = Board(width, height)

    """ Opening the instrucion_list.txt file and retrieving the instructions to move the robot"""
    instructions = open('./instrucion_list.txt', 'r')
    while 1:
        instruction = instructions.readline().split(',')
        if instruction[0] == 'right' or instruction[0] == 'left':
            direction = str(instruction[0])
            steps = int(instruction[1].strip())
            position = board.move(direction, steps)  # Retrieving of the last position
        else:
            break
    instructions.close()

    print(position)  # Position display


if __name__ == "__main__":
    main()
