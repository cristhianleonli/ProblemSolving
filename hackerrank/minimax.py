#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    sorted_list = sorted(arr)
    return (sum(sorted_list[:4]), sum(sorted_list[-4:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    (minimun, maximum) = miniMaxSum(arr)
    print(minimun, maximum)
