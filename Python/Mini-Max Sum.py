# # Given five positive integers, find the minimum and maximum values 
# that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single 
# line of two space-separated long integers.
# 
# Input Format
# 
# A single line of five space-separated integers.
# 
# Constraints
# 
# Each integer is in the inclusive range .
# 
# Output Format
# 
# Print two space-separated long integers denoting the respective 
# minimum and maximum values that can be calculated by summing exactly 
# four of the five integers. 
# 
# (The output can be greater than a 32 bit integer.)
# 
# Sample Input
# 
# 1 2 3 4 5
# 
# Sample Output
# 
# 10 14
# 
# Explanation
# 
# Our initial numbers are 1, 2, 3, 4, and 5. We can calculate the 
# following sums using four of the five integers:
# 
# If we sum everything except 1, our sum is 2+3+4+5=14.
# If we sum everything except 2, our sum is 1+3+4+5=13.
# If we sum everything except 3, our sum is 1+2+4+5=12.
# If we sum everything except 4, our sum is 1+2+3+5=11.
# If we sum everything except 5, our sum is 1+2+3+4=10.
# 
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    l = len(arr)
    a=0
    b=l-1
    i=0
    min_sum = 0
    max_sum = 0
    for x in arr:
        min_sum = min_sum + arr[i]
        max_sum = max_sum + arr[i]
        i = i + 1
    min_sum = min_sum - arr[b]
    max_sum = max_sum - arr[a]
    print min_sum, max_sum

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
