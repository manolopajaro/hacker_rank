#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#def diagonalDifference(arr):



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    sum_1 = 0
    sum_2 = 0
    for i in range(n):
        row = list(map(int, input().rstrip().split()))
        arr.append(row)
        sum_1 += row[i]
        sum_2 += row[(i+1)*-1]
    print(abs(sum_1-sum_2))
    #result = diagonalDifference(arr)
    #print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
