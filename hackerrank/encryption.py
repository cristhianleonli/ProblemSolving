#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


def add_lists(a, b):
    result = [""] * min(len(a), len(b))
    for i in range(0, min(len(a), len(b))):
        result[i] = a.pop(0) + b.pop(0)

    if len(a) > 0:
        result += a

    if len(b) > 0:
        result += b

    return result


def encryption(s):
    string = s.replace(" ", "")
    n = math.sqrt(len(string))

    upper = math.ceil(n)
    gen = [string[i:i+upper] for i in range(0, len(string), upper)]
    result = reduce(lambda acc, y: add_lists(acc, list(y)), gen, [])
    return " ".join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
