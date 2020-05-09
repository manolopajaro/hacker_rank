#!/bin/python3

import os
import sys
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    date = datetime.strptime(s,'%I:%M:%S%p')
    return date.strftime('%H:%M:%S')



if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = "07:05:45PM"#input()

    result = timeConversion(s)
    print(result)
    #f.write(result + '\n')

    #f.close()
