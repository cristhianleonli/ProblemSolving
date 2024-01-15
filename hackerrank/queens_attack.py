#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def translate_position(position, size):
    return [size - position[0], position[1] - 1]

def find_diagonal(queen, obstacles, size, pos):
    positions = []

    if pos == 'tr':
        i, j = queen[0] - 1, queen[1] + 1
        while i >= 0 and j < size:
            p = [i, j]
            if p in obstacles:
                break
            positions.append(p)
            i, j = i - 1, j + 1
    elif pos == 'tl':
        i, j = queen[0] - 1, queen[1] - 1
        while i >= 0 and j >= 0:
            p = [i, j]
            if p in obstacles:
                break
            positions.append(p)
            i, j = i - 1, j - 1
    elif pos == 'br':
        i, j = queen[0] + 1, queen[1] + 1
        while i < size and j < size:
            p = [i, j]
            if p in obstacles:
                break
            positions.append(p)
            i, j = i + 1, j + 1
    elif pos == 'bl':
        i, j = queen[0] + 1, queen[1] - 1
        while i < size and j >= 0:
            p = [i, j]
            if p in obstacles:
                break
            positions.append(p)
            i, j = i + 1, j - 1
    
    return len(positions)

def find_hv(queen, obstacles, size, pos):
    positions = []

    if pos == 't':
        i = queen[0] - 1
        while i >= 0:
            p = [i, queen[1]]
            if p in obstacles:
                break
            positions.append(p)
            i -= 1
    elif pos == 'b':
        for i in range(queen[0] + 1, size):
            p = [i, queen[1]]

            if p in obstacles:
                break
            positions.append(p)
    elif pos == 'r':
        for i in range(queen[1] + 1, size):
            p = [queen[0], i]

            if p in obstacles:
                break
            positions.append(p)
    elif pos == 'l':
        i = queen[1] - 1
        while i >= 0:
            p = [queen[0], i]
            if p in obstacles:
                break
            positions.append(p)
            i -= 1
    
    return len(positions)

def queens_attack(n, k, r_q, c_q, obstacles):
    queen_position = translate_position([r_q, c_q], size=n)
    obstacles_positions = []

    for obstacle in obstacles:
        obstacles_positions.append(translate_position(obstacle, size=n))

    right = find_hv(queen_position, obstacles_positions, size=n, pos='r')
    left = find_hv(queen_position, obstacles_positions, size=n, pos='l')
    bottom = find_hv(queen_position, obstacles_positions, size=n, pos='b')
    top = find_hv(queen_position, obstacles_positions, size=n, pos='t')

    top_right = find_diagonal(queen_position, obstacles_positions, size=n, pos='tr')
    top_left = find_diagonal(queen_position, obstacles_positions, size=n, pos='tl')
    bottom_right = find_diagonal(queen_position, obstacles_positions, size=n, pos='br')
    bottom_left = find_diagonal(queen_position, obstacles_positions, size=n, pos='bl')

    return right + left + bottom + top + top_right + top_left + bottom_right + bottom_left

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = '5 3'.split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = '4 3'.split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = [
        [5, 5],
        [4, 2],
        [2, 3]
    ]

    result = queens_attack(n, k, r_q, c_q, obstacles)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
