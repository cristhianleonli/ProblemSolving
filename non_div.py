#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    residuals = [i % k for i in s]
    counter = [0] * k
    for r in residuals:
        counter[r] += 1

    # max one element with residual 0
    c = min(counter[0], 1)

    for i in range(1, (k//2)+1):
        if i != k-i:
            c += max(counter[i], counter[k-i])
        else:
            c += min(counter[i], 1)

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
