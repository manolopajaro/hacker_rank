#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    max_list = arr.copy()
    min_list = arr.copy()
    del max_list[0]
    del min_list[-1]
    print(str(sum(min_list))+" "+str(sum(max_list)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
