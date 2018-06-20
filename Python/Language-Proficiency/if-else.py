Task 
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0

n=3 
n is odd and odd numbers are weird, so we print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1

n=24 
n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.

Current Buffer (saved locally, editable)    
 
 
 
 
1
#!/bin/python
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
​
10
if __name__ == '__main__':
11
    n = int(raw_input())
12
​
13
    
14
if n % 2 != 0:
15
    print 'Weird'
16
elif n >= 2 and n <= 5:
17
    print 'Not Weird'
18
elif n >= 6 and n <= 20:
19
    print 'Weird'
20
elif n > 20:
21
    print 'Not Weird'
22
​
23
​
24
    
