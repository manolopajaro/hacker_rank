#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    spring = -1
    height = 1
    for _ in range(n):
        if spring == -1:
            height *= 2
        else:
            height += 1
        spring *= -1
    return height;

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(str(result) + '\n')

    #fptr.close()
