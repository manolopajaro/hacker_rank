#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    rev_arr = reversed(arr)
    output = ""
    for n in rev_arr:
        output += str(n) + " "
    print(output)