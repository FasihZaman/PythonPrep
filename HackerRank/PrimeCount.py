#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def is_prime(m):
    for j in range(2,m):
        if (m%j) == 0:
            return False
    return True
    
def primeCount(n):
    prod = 1
    c = 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,n):
            if is_prime(i):
                prod *= i
                if prod<=n:
                    c+=1
                else:
                    break
    
    return c 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
