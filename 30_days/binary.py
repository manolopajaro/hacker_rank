#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary = "{0:b}".format(n)
    count = 0
    consec = []
    for i in binary:
        if i == "1":
            count += 1
        elif count > 0:
            consec.append(count)
            count = 0
    consec.append(count)
    print(max(consec))
