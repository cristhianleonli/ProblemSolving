#!/bin/python3

import math
import os
import random
import re
import sys

memo = {}


def factorial(n):
    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    f = n * factorial(n-1)
    memo[n] = f
    return f

# Complete the extraLongFactorials function below.


def extraLongFactorials(n):
    print(factorial(n))


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
