# Problem: Weird - https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else:
        if n<= 5:
            print("Not Weird")
            
        elif n<= 20:
            print("Weird")
            
        else:
            print("Not Weird")
            
