# Problem: Array Manipulation - https://www.hackerrank.com/challenges/crush/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    prefix_sum=[0] * n 
    for a in queries:
        start = a[0] 
        end = a[1] 
        val = a[2]
        # print(val)
        prefix_sum[start - 1] += val
        if end < (n):
            prefix_sum[end] -= val
        # print(prefix_sum)
    running_sum = 0
    sum_max = 0
    for a in prefix_sum:
        running_sum += a
        sum_max = max(running_sum, sum_max)
    return sum_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
