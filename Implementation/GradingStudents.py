#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    scores = []
    for grade in grades:
        if grade < 38 or grade % 5 == 0:
            scores.append(grade)
        else:
            next_multiplo = (int(grade / 5) + 1) * 5
            if next_multiplo - grade < 3:
                scores.append(next_multiplo)
            else:
                scores.append(grade)
    return scores

def gradingStudents2(grades):
    # Write your code here
    scores = []
    for grade in grades:
        sobrante = grade % 5
        if grade >= 38 and sobrante >= 3:
            scores.append(grade+(5-sobrante))
        else:
            scores.append(grade)
    return scores


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents2(grades)
    print(result)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
