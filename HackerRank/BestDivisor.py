#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    divisors = (i for i in range(1,n+1) if not n % i)
    best = lambda x: sum(int(i) for i in str(x))
    print (max(divisors, key=best))
