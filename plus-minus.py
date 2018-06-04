# Given an array of integers, calculate the fractions of its elements that are 
# positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
# 
# Note: This challenge introduces precision problems. The test cases are scaled to six 
# decimal places, though answers with absolute error of up to  are acceptable.
# 
# Input Format
#
# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers describing an array of numbers .
#
# Output Format
#
# You must print the following  lines:
# 
# A decimal representing of the fraction of positive numbers in the array compared to its size.
# A decimal representing of the fraction of negative numbers in the array compared to its size.
# A decimal representing of the fraction of zeros in the array compared to its size.
# 
# Sample Input
# 
# 6
# -4 3 -9 0 4 1         
# 
# Sample Output
# 
# 0.500000
# 0.333333
# 0.166667
# 
# Explanation
# 
# There are  positive numbers,  negative numbers, and  zero in the array. 
# The proportions of occurrence are positive: , negative:  and zeros: .
# 
# 
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a=len(arr)
    p=0
    n=0
    z=0
    for x in arr:
        if x > 0:
            p=p+1
        if x < 0:
            n=n+1
        if x == 0:
            z=z+1
    print p / float(a)
    print n / float(a)
    print z / float(a)
    
        

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
