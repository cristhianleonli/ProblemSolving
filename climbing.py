#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def binary_search(a, key):
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if a[mid] == key:
            return mid
        if a[mid] < key and key < a[mid - 1]:
            return mid
        if a[mid] > key and key >= a[mid + 1]:
            return mid + 1
        if a[mid] < key:
            hi = mid - 1
        elif a[mid] > key:
            lo = mid + 1
        
    return -1

def climbingLeaderboard(ranked, player):
    table = []
    ranks = [1]
    
    for i in range(1, len(ranked)):
        if ranked[i-1] == ranked[i]:
            ranks.append(ranks[i-1])
        else:
            ranks.append(ranks[i-1] + 1)

    result = []
    for i in range(len(player)):
        score = player[i]
        if score > ranked[0]:
            result.append(1)
        elif score < ranked[-1]:
            result.append(ranks[-1] + 1)
        else:
            index = binary_search(ranked, score)
            result.append(ranks[index])
    
    return result

if __name__ == '__main__':
    p = climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
    q = climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
    print(p)
    print(q)
