#!/bin/python3

import math
import os
import random
import re
import sys


def check(a, b):
    if a > b:
        return 0
    if a < b:
        return 1
    return None


def compareTriplets(a, b):
    result = [0, 0]
    for i in range(0, len(a)):
        pos = check(a[i], b[i])
        if pos is not None:
            result[pos] += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
