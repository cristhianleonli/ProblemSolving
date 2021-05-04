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

def locate_opponents(opponents, r_q, c_q):
    memo = {
        "t": [], "b": [], "r": [], "l": [],
        "tr": [], "br": [], "bl": [], "tl": []
    }

    for opponent in opponents:
        if opponent[1] == c_q and opponent[0] > r_q:
            memo["t"].append(opponent)

        if opponent[1] == c_q and opponent[0] < r_q:
            memo["b"].append(opponent)

        if opponent[0] == r_q and opponent[1] > c_q:
            memo["r"].append(opponent)

        if opponent[0] == r_q and opponent[1] < c_q:
            memo["l"].append(opponent)

        diff_r = opponent[0] - r_q
        diff_c = opponent[1] - c_q

        if abs(diff_r) == abs(diff_c):
            if diff_r >= 0 and diff_c >= 0:
                memo["tr"].append(opponent)

            if diff_r >= 0 and diff_c < 0:
                memo["tl"].append(opponent)

            if diff_r < 0 and diff_c >= 0:
                memo["br"].append(opponent)

            if diff_r < 0 and diff_c < 0:
                memo["bl"].append(opponent)

    return memo

def find_horizontal(queen, border, obstacles):
    positions = []

    if pos == 't':
        pass
    elif pos == 'tr':
        pass
    elif pos == 'tr':
        pass
    elif pos == 'tr':
        pass
    elif pos == 'tr':
        pass
    elif pos == 'tr':
        pass
    elif pos == 'tr':
        pass
    elif pos == 'tr':
        pass

    for i in range(queen[0] + 1, border[0]):
        p = [i, queen[1]]
        if p in obstacles:
            break
        positions.append(p)
    
    return positions

def queens_attack(n, k, r_q, c_q, obstacles):
    obstacles_positions = []

    for obstacle in obstacles:
        obstacles_positions.append(translate_position(obstacle, size=n))
    
    queen_position = translate_position([r_q, c_q], size=n)

    # print(obstacles_positions)
    # print(queen_position)

    right = find_horizontal(queen_position, [n-1, queen_position[1]], obstacles)
    print(right)

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
        [4, 3],
        [2, 3]
    ]

    result = queens_attack(n, k, r_q, c_q, obstacles)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
