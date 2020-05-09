#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        arr = list(range(1, n + 1))
        # print(arr)
        selected = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                bitwise = arr[i] & arr[j]
                # print("A = "+str(arr[i])+" B = "+str(arr[j])+" A&B = "+str(bitwise))
                if bitwise < k:
                    selected.append(bitwise)
        selected.sort()
        # print(selected)
        print(selected[-1])
