# Consider a staircase of size :
# 
#    #
#   ##
#  ###
# ####
# 
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# 
# Write a program that prints a staircase of size .
# 
# Input Format
# 
# A single integer, , denoting the size of the staircase.
# 
# Output Format
# 
# Print a staircase of size  using # symbols and spaces.
# 
# Note: The last line must have  spaces in it.
# 
# Sample Input
# 
# 6 
# Sample Output
# 
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# 
# Explanation
# 
# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
# 
# 
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    s=1
    y=n-s
    for x in range (n):
        print (" " * y) + ("#" * s)
        s=s+1
        y=y-1
    

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
