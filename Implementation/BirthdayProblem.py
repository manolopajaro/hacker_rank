#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthday function below.


def birthday(s, d, m):
    counter = 0
    for i in range(len(s)-(m-1)):
        counter_aux = 0
        for j in range(i,i+m):
            counter_aux += s[j]
        if counter_aux == d:
            counter += 1
    return counter

#https://www.hackerrank.com/challenges/the-birthday-bar/problem
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
